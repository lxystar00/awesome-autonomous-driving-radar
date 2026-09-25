"""Company tracking: Google News RSS, official blog feeds, new GitHub repos."""
from __future__ import annotations

import hashlib
import re
import time
from datetime import timedelta
from email.utils import parsedate_to_datetime
from urllib.parse import quote

import feedparser

from common import COMPANIES, CONFIG, gh_token_headers, http, log, now_utc

GNEWS = "https://news.google.com/rss/search?q={q}+when:{days}d&hl={hl}&gl={gl}&ceid={ceid}"
EXCLUDE = re.compile(CONFIG["news"]["exclude_regex"], re.I)


def _date(e) -> str:
    for k in ("published", "updated"):
        if e.get(k):
            try:
                return parsedate_to_datetime(e[k]).strftime("%Y-%m-%d")
            except (TypeError, ValueError):
                return e[k][:10]
    return now_utc().strftime("%Y-%m-%d")


def _item(company: str, kind: str, title: str, url: str, date: str, source: str) -> dict:
    title = " ".join(title.split())
    key = re.sub(r"[^a-z0-9]+", "", title.lower())[:80]
    return {"id": hashlib.sha1(f"{company}|{key}".encode()).hexdigest()[:12],
            "company": company, "kind": kind, "title": title, "url": url,
            "date": date, "source": source}


def _feed(url: str):
    r = http("GET", url, timeout=30, retries=2)
    return feedparser.parse(r.content) if r is not None and r.ok else None


def google_news(company: dict, days: int) -> list[dict]:
    out = []
    variants = [("news", "en-US", "US", "US:en")]
    if company.get("news_zh"):
        variants.append(("news_zh", "zh-CN", "CN", "CN:zh-Hans"))
    for field, hl, gl, ceid in variants:
        url = GNEWS.format(q=quote(company[field]), days=days, hl=hl, gl=gl, ceid=ceid)
        f = _feed(url)
        if not f:
            continue
        for e in f.entries[:30]:
            title = e.get("title", "")
            src = (e.get("source") or {}).get("title", "")
            if src and title.endswith(" - " + src):
                title = title[: -len(src) - 3]
            if EXCLUDE.search(title):
                continue
            out.append(_item(company["name"], "news", title, e.link, _date(e), src or "Google News"))
        time.sleep(1)
    return out


def blog_feeds(company: dict) -> list[dict]:
    out = []
    for url in company.get("feeds", []):
        f = _feed(url)
        if not f:
            log.warning("feed failed: %s", url)
            continue
        for e in f.entries[:20]:
            out.append(_item(company["name"], "blog", e.get("title", ""), e.get("link", url),
                             _date(e), "official blog"))
    return out


def new_repos(company: dict, since: str) -> list[dict]:
    out = []
    for org in company.get("github", []):
        r = http("GET", f"https://api.github.com/orgs/{org}/repos",
                 params={"sort": "created", "direction": "desc", "per_page": 10},
                 headers=gh_token_headers(), retries=2, timeout=20)
        if r is None or r.status_code != 200:
            r = http("GET", f"https://api.github.com/users/{org}/repos",
                     params={"sort": "created", "direction": "desc", "per_page": 10},
                     headers=gh_token_headers(), retries=1, timeout=20)
        if r is None or r.status_code != 200:
            continue
        for d in r.json():
            if d.get("fork") or (d.get("created_at") or "")[:10] < since:
                continue
            desc = f" — {d['description']}" if d.get("description") else ""
            out.append(_item(company["name"], "repo", f"{d['full_name']}{desc}", d["html_url"],
                             d["created_at"][:10], "GitHub"))
    return out


def fetch(days: int = 2) -> list[dict]:
    since = (now_utc() - timedelta(days=days)).strftime("%Y-%m-%d")
    items: list[dict] = []
    for c in COMPANIES:
        got = google_news(c, days) + blog_feeds(c) + new_repos(c, since)
        got = [g for g in got if g["date"] >= since]
        log.info("news %-16s %d items", c["name"], len(got))
        items.extend(got)
    return items


def merge(store: dict, items: list[dict]) -> list[dict]:
    """Insert unseen items into store (keyed by id). Returns the newly added items."""
    added = []
    for it in items:
        if it["id"] not in store:
            store[it["id"]] = it
            added.append(it)
    cutoff = (now_utc() - timedelta(days=CONFIG["news"]["keep_days"])).strftime("%Y-%m-%d")
    for k in [k for k, v in store.items() if v["date"] < cutoff]:
        del store[k]
    return added
