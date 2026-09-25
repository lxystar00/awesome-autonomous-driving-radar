"""Quality signals: Semantic Scholar (venue, citations), Hugging Face (code, stars,
upvotes), GitHub (stars, activity), plus local venue / org detection."""
from __future__ import annotations

import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta

from common import COMPANIES, CONFIG, gh_token_headers, http, log, now_utc, parse_date

S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"
S2_FIELDS = "externalIds,citationCount,influentialCitationCount,venue,publicationVenue,year"
HF_PAPER = "https://huggingface.co/api/papers/{}"
GH_REPO = "https://api.github.com/repos/{}/{}"

KNOWN_ORGS = {o.lower() for o in CONFIG["known_orgs"]}
for c in COMPANIES:
    KNOWN_ORGS.update(o.lower() for o in c.get("github", []))


def _stale(ts: str | None, days: float) -> bool:
    return not ts or now_utc() - parse_date(ts) >= timedelta(days=days)


def _stamp() -> str:
    return now_utc().strftime("%Y-%m-%d")


# ---------------------------------------------------------------- venue detection

def _venue_patterns():
    pats = []
    for tier, venues in CONFIG["venues"].items():
        for short, aliases in venues.items():
            for a in aliases:
                pats.append((tier, short, re.compile(r"(?<![A-Za-z])" + re.escape(a) + r"(?![A-Za-z])", re.I)))
    return pats


_VENUES = _venue_patterns()
_YEAR = re.compile(r"(?:20)?(2[5-7])\b")
_NEGATIVE = re.compile(r"\b(workshop|submitted to|under review|in submission|rejected)\b", re.I)


def detect_venue(p: dict) -> tuple[str | None, str | None]:
    """Return (tier, label) e.g. ("top", "CVPR 2026"). Author-provided comments and
    journal_ref come first; Semantic Scholar's venue is the fallback."""
    sources = [p.get("comments", ""), p.get("journal_ref", ""), p.get("s2_venue", "")]
    for i, text in enumerate(sources):
        if not text:
            continue
        # Workshops and "submitted to X" do not count as acceptance.
        if _NEGATIVE.search(text):
            continue
        for tier, short, pat in _VENUES:
            m = pat.search(text)
            if not m:
                continue
            y = _YEAR.search(text[m.end():m.end() + 12])
            year = f"20{y.group(1)}" if y else (str(p["s2_year"]) if p.get("s2_year") and i == 2 else "")
            return tier, f"{short} {year}".strip()
    return None, None


# ---------------------------------------------------------------- Semantic Scholar

def enrich_s2(papers: list[dict], refresh_days: float = 3) -> None:
    todo = [p for p in papers if _stale(p.get("s2_at"), refresh_days)]
    log.info("S2: %d papers to refresh", len(todo))
    for i in range(0, len(todo), 400):
        chunk = todo[i:i + 400]
        r = http("POST", S2_BATCH, params={"fields": S2_FIELDS},
                 json={"ids": [f"ARXIV:{p['id']}" for p in chunk]}, timeout=60, retries=6, backoff=5)
        if r is None or not r.ok:
            log.warning("S2 batch failed (%d papers); continuing without it", len(chunk))
            continue
        for p, d in zip(chunk, r.json()):
            p["s2_at"] = _stamp()
            if not d:
                continue
            p["citations"] = d.get("citationCount") or 0
            p["influential_citations"] = d.get("influentialCitationCount") or 0
            venue = d.get("venue") or ""
            pv = (d.get("publicationVenue") or {}).get("name") or ""
            v = " / ".join(x for x in {venue, pv} if x and x.lower() not in {"arxiv.org", "arxiv"})
            p["s2_venue"] = v
            p["s2_year"] = d.get("year")
        time.sleep(3)


# ---------------------------------------------------------------- Hugging Face

def _hf_one(p: dict) -> None:
    r = http("GET", HF_PAPER.format(p["id"]), timeout=20, retries=3)
    p["hf_at"] = _stamp()
    if r is None or r.status_code != 200:
        return
    d = r.json()
    p["hf_upvotes"] = d.get("upvotes") or 0
    repo = d.get("githubRepo")
    if repo and "github.com" in repo:
        p.setdefault("code_url", None)
        p["code_url"] = p["code_url"] or repo.rstrip("/")
        if d.get("githubStars") is not None and (p["code_url"].lower() == repo.rstrip("/").lower()):
            p["stars"] = d["githubStars"]
            p["stars_at"] = _stamp()


def enrich_hf(papers: list[dict], refresh_days: float = 7, workers: int = 6) -> None:
    todo = [p for p in papers if _stale(p.get("hf_at"), refresh_days)]
    log.info("HF: %d papers to refresh", len(todo))
    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(_hf_one, todo))


# ---------------------------------------------------------------- GitHub

def _split_repo(url: str) -> tuple[str, str] | None:
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)", url or "")
    return (m.group(1), m.group(2)) if m else None


def enrich_github(papers: list[dict], budget: int, refresh_days: float = 3) -> int:
    """Refresh stars for papers with a code URL; papers lacking stars go first."""
    todo = [p for p in papers if p.get("code_url") and _stale(p.get("stars_at"), refresh_days)]
    todo.sort(key=lambda p: (p.get("stars") is not None, -(p.get("score") or 0)))
    used = 0
    headers = gh_token_headers()
    for p in todo:
        if used >= budget:
            break
        parts = _split_repo(p["code_url"])
        if not parts:
            continue
        r = http("GET", GH_REPO.format(*parts), headers=headers, retries=2, backoff=2, timeout=20)
        used += 1
        if r is None:
            # Most likely rate-limited; stop instead of burning retries.
            log.warning("GitHub API unavailable after %d calls; stopping", used)
            break
        p["stars_at"] = _stamp()
        if r.status_code == 404:
            p["code_status"] = "missing"
            continue
        d = r.json()
        p["stars"] = d.get("stargazers_count", 0)
        p["code_pushed"] = (d.get("pushed_at") or "")[:10]
        p["code_status"] = "ok"
        if d.get("html_url"):
            p["code_url"] = d["html_url"]  # follow renames / redirects
    log.info("GitHub: %d API calls", used)
    return used


_LIST_REPO = re.compile(r"awesome|daily|arxiv|paper|list|survey|reading|digest|collection", re.I)
_STOP = {"a", "an", "the", "for", "of", "and", "in", "on", "with", "via", "to", "towards", "from",
         "autonomous", "driving", "learning", "model", "models", "end"}


def _title_tokens(title: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", title.lower()) if len(w) > 2 and w not in _STOP}


def _plausible_repo(p: dict, full_name: str) -> bool:
    """Repo name must look like it belongs to this paper, not a paper-list repo."""
    name = full_name.split("/", 1)[1]
    if _LIST_REPO.search(name):
        return False
    rn = re.sub(r"[^a-z0-9]", "", name.lower())
    head = re.split(r"[:\-–]", p["title"])[0].strip()
    acronym = re.sub(r"[^a-z0-9]", "", head.lower())
    if len(head.split()) <= 2 and len(acronym) >= 3 and acronym in rn:
        return True
    toks = set(re.findall(r"[a-z0-9]+", name.lower().replace("_", "-")))
    return len(toks & _title_tokens(p["title"])) >= 2


def discover_code(papers: list[dict], budget: int) -> int:
    """GitHub search fallback for promising papers with no code link: look for the
    arXiv id in READMEs. Search API allows 10 req/min unauthenticated, 30 with a token."""
    todo = [p for p in papers if not p.get("code_url") and _stale(p.get("code_search_at"), 7)
            and (p.get("venue_tier") or (p.get("llm") or {}).get("quality", 0) >= 6)]
    todo.sort(key=lambda p: -(p.get("score") or 0))
    headers = gh_token_headers()
    delay = 2.2 if "Authorization" in headers else 6.5
    found = 0
    for p in todo[:budget]:
        r = http("GET", "https://api.github.com/search/repositories", headers=headers,
                 params={"q": f'"{p["id"]}" in:readme', "per_page": 10}, retries=2, backoff=10)
        time.sleep(delay)
        if r is None or r.status_code != 200:
            log.warning("GitHub search unavailable; stopping discovery")
            break
        p["code_search_at"] = _stamp()
        for it in r.json().get("items", []):
            if _plausible_repo(p, it["full_name"]):
                p["code_url"], p["stars"] = it["html_url"], it["stargazers_count"]
                p["stars_at"], p["code_status"], p["code_found_by"] = _stamp(), "ok", "search"
                found += 1
                break
    log.info("GitHub search: checked %d, found code for %d", min(len(todo), budget), found)
    return found


# ---------------------------------------------------------------- local signals

def compute_signals(p: dict) -> None:
    tier, label = detect_venue(p)
    p["venue_tier"], p["venue"] = tier, label
    parts = _split_repo(p.get("code_url") or "")
    p["known_org"] = bool(parts and parts[0].lower() in KNOWN_ORGS)
    age = max((now_utc() - parse_date(p["published"])).days / 30.44, 1.0)
    p["age_months"] = round(age, 1)
    p["cites_per_month"] = round((p.get("citations") or 0) / age, 2)
