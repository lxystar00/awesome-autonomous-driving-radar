"""Topic assignment, composite score, hard filter and curated selection."""
from __future__ import annotations

import math

from common import CONFIG

TOPICS = CONFIG["topics"]
BENCH = [b.lower() for b in CONFIG["benchmarks"]]
SOTA_WORDS = ("state-of-the-art", "state of the art", "sota", "outperforms", "surpasses")


def heuristic_topic(p: dict) -> str:
    title, abstract = p["title"].lower(), p["abstract"].lower()
    best, best_score = "e2e", 0
    for key, t in TOPICS.items():
        s = sum(3 * title.count(term) + abstract.count(term) for term in t["terms"])
        if s > best_score:
            best, best_score = key, s
    return best


def topic(p: dict) -> str:
    return (p.get("llm") or {}).get("topic") or heuristic_topic(p)


def _log_scale(x: float, full: float) -> float:
    """0 at x=0, 1 at x=full, saturating above."""
    return min(math.log1p(max(x, 0)) / math.log1p(full), 1.0)


def score(p: dict) -> float:
    """Composite quality score in [0, 100]."""
    s = 0.0
    s += {"top": 30, "strong": 18}.get(p.get("venue_tier"), 0)
    if p.get("code_url") and p.get("code_status") != "missing":
        s += 5
        # Stars per month keeps new repos competitive with old ones.
        stars = p.get("stars") or 0
        s += 10 * _log_scale(stars, 2000) + 5 * _log_scale(stars / p.get("age_months", 1), 150)
    s += 15 * _log_scale(p.get("cites_per_month", 0), 20)
    s += 3 * _log_scale(p.get("influential_citations", 0), 20)
    s += 3 * _log_scale(p.get("hf_upvotes", 0), 50)
    if p.get("known_org"):
        s += 4
    llm = p.get("llm") or {}
    if llm.get("quality") is not None:
        s += 25 * max(llm["quality"] - 4, 0) / 5  # 4 -> 0, 9 -> 25
        s += 3 if llm.get("sota") else 0
    else:
        text = p["abstract"].lower()
        s += 4 if any(w in text for w in SOTA_WORDS) else 0
        s += 4 if any(b in text for b in BENCH) else 0
    return round(min(s, 100), 1)


def driving_focus(p: dict) -> int:
    """Crude relevance strength used until the LLM verdict is available:
    title hits count 3, abstract hits 1."""
    terms = CONFIG["relevance_terms"]
    title, abstract = p["title"].lower(), p["abstract"].lower()
    return sum(3 * (t in title) + abstract.count(t) for t in terms)


def has_code(p: dict) -> bool:
    return bool(p.get("code_url")) and p.get("code_status") != "missing"


def strong_signal(p: dict) -> bool:
    return (p.get("venue_tier") in ("top", "strong")
            or (p.get("stars") or 0) >= 200
            or p.get("cites_per_month", 0) >= 3
            or (p.get("known_org") and (p.get("stars") or 0) >= 50))


def eligible(p: dict) -> bool:
    """Hard filter for the curated list."""
    ex, inc = CONFIG["curation"]["exclude"] or [], CONFIG["curation"]["include"] or []
    if p["id"] in ex:
        return False
    if p["id"] in inc:
        return True
    llm = p.get("llm") or {}
    if llm and not llm.get("relevant", True):
        return False
    if not llm and driving_focus(p) < 2:
        return False
    if llm.get("quality") is not None and llm["quality"] < 5:
        return False
    return has_code(p) and strong_signal(p)


def curate(papers: list[dict], window_start: str) -> list[dict]:
    """Top-N eligible papers in the window with a per-topic cap."""
    size, cap = CONFIG["curated_size"], CONFIG["per_topic_cap"]
    pool = sorted((p for p in papers if p["published"] >= window_start and eligible(p)),
                  key=lambda p: p["score"], reverse=True)
    chosen, per_topic = [], {}
    for p in pool:
        t = p["topic"]
        if per_topic.get(t, 0) >= cap and p["id"] not in (CONFIG["curation"]["include"] or []):
            continue
        chosen.append(p)
        per_topic[t] = per_topic.get(t, 0) + 1
        if len(chosen) >= size:
            break
    return chosen


def llm_candidates(papers: list[dict], n: int) -> list[dict]:
    """Papers worth an LLM call: those that could plausibly make the curated list."""
    pool = [p for p in papers if "llm" not in p and (has_code(p) or p.get("venue_tier"))]
    pool.sort(key=lambda p: p["score"], reverse=True)
    return pool[:n]
