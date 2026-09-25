"""Harvest autonomous-driving papers from arXiv via OAI-PMH.

The arXiv search API (export.arxiv.org/api/query) is often blocked for CI / proxy
IPs, while OAI-PMH is arXiv's official bulk-harvest interface. We harvest the
configured category sets by datestamp (last-modified date), then keep papers whose
first version falls inside the window and whose title/abstract is driving-related.
"""
from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from datetime import timedelta

from common import CONFIG, http, log, parse_date

OAI = "https://oaipmh.arxiv.org/oai"
NS = {"o": "http://www.openarchives.org/OAI/2.0/", "a": "http://arxiv.org/OAI/arXiv/"}
GH_RE = re.compile(r"https?://github\.com/([\w.-]+)/([\w.-]+)", re.I)
_GH_SKIP = {"orgs", "topics", "features", "sponsors", "settings", "marketplace"}


def extract_github(text: str) -> str | None:
    for owner, repo in GH_RE.findall(text or ""):
        repo = repo.rstrip(".").removesuffix(".git")
        if owner.lower() in _GH_SKIP or not repo:
            continue
        return f"https://github.com/{owner}/{repo}"
    return None


def _txt(el, path: str) -> str:
    x = el.find(path, NS)
    return " ".join((x.text or "").split()) if x is not None else ""


def first_version_date(aid: str, created: str) -> str:
    """OAI `created` is not always the v1 date, but a new-style id (YYMM.NNNNN) pins
    the v1 month. Use `created` when it agrees with that month, else the month start."""
    m = re.match(r"(\d{2})(\d{2})\.\d{4,5}$", aid)
    if not m:
        return created
    ym = f"20{m.group(1)}-{m.group(2)}"
    return created if created.startswith(ym) else f"{ym}-01"


def _record_to_paper(meta) -> dict:
    aid = _txt(meta, "a:id")
    created = _txt(meta, "a:created")[:10]
    authors = []
    for au in meta.findall("a:authors/a:author", NS):
        name = " ".join(filter(None, [_txt(au, "a:forenames"), _txt(au, "a:keyname")]))
        if name:
            authors.append(name)
    abstract = _txt(meta, "a:abstract")
    comments = _txt(meta, "a:comments")
    return {
        "id": aid,
        "title": _txt(meta, "a:title"),
        "authors": authors,
        "abstract": abstract,
        "comments": comments,
        "journal_ref": _txt(meta, "a:journal-ref"),
        "published": first_version_date(aid, created),
        "updated": (_txt(meta, "a:updated") or created)[:10],
        "categories": _txt(meta, "a:categories").split(),
        "url": f"https://arxiv.org/abs/{aid}",
        "code_url": extract_github(abstract + " " + comments),
    }


def is_relevant(p: dict) -> bool:
    text = (p["title"] + " " + p["abstract"]).lower()
    return any(t in text for t in CONFIG["relevance_terms"])


def _harvest(set_spec: str, d0: str, d1: str):
    params = {"verb": "ListRecords", "metadataPrefix": "arXiv", "set": set_spec,
              "from": d0, "until": d1}
    while True:
        r = http("GET", OAI, params=params, timeout=120, backoff=10)
        if r is None or not r.ok:
            raise RuntimeError(f"OAI-PMH request failed for {set_spec} {d0}..{d1}")
        root = ET.fromstring(r.content)
        err = root.find("o:error", NS)
        if err is not None:
            if err.get("code") == "noRecordsMatch":
                return
            raise RuntimeError(f"OAI-PMH error {err.get('code')}: {err.text}")
        lr = root.find("o:ListRecords", NS)
        for rec in lr.findall("o:record", NS):
            meta = rec.find("o:metadata/a:arXiv", NS)
            if meta is not None:
                yield meta
        tok = lr.find("o:resumptionToken", NS)
        if tok is None or not (tok.text or "").strip():
            return
        params = {"verb": "ListRecords", "resumptionToken": tok.text.strip()}
        time.sleep(3)


def fetch(since: str, until: str, *, created_after: str) -> list[dict]:
    """Harvest records modified in [since, until]; keep papers first submitted on or
    after `created_after` that pass the relevance check. Dates are YYYY-MM-DD."""
    sets = CONFIG["arxiv"]["oai_sets"]
    step = timedelta(days=CONFIG["arxiv"].get("chunk_days", 7))
    seen: dict[str, dict] = {}
    scanned = 0
    start, end = parse_date(since), parse_date(until)
    while start <= end:
        stop = min(start + step - timedelta(days=1), end)
        d0, d1 = start.strftime("%Y-%m-%d"), stop.strftime("%Y-%m-%d")
        for s in sets:
            n0 = scanned
            for meta in _harvest(s, d0, d1):
                scanned += 1
                p = _record_to_paper(meta)
                if p["published"] < created_after or not is_relevant(p):
                    continue
                seen[p["id"]] = p  # later datestamps overwrite (fresher comments)
            log.info("OAI %s %s..%s: %d records", s, d0, d1, scanned - n0)
            time.sleep(2)
        start = stop + timedelta(days=1)
    log.info("arXiv: scanned %d records, %d relevant", scanned, len(seen))
    return list(seen.values())
