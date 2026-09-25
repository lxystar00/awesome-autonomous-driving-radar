"""Shared helpers: paths, config, HTTP with retry, JSON storage, dates."""
from __future__ import annotations

import json
import logging
import os
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UA = "ad-radar/0.1 (+https://github.com/; autonomous-driving paper tracker)"

log = logging.getLogger("ad-radar")


def setup_logging(verbose: bool = False) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)


def load_yaml(name: str):
    with open(ROOT / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


CONFIG = load_yaml("config.yaml")
COMPANIES = load_yaml("companies.yaml")


def load_json(path: Path, default):
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    tmp.replace(path)


_session = requests.Session()
_session.headers["User-Agent"] = UA


def http(method: str, url: str, *, retries: int = 4, backoff: float = 3.0,
         ok_status=(200,), **kw) -> requests.Response | None:
    """HTTP with retry on 429/5xx/network errors. Returns None when all attempts fail
    or the final status is not in ok_status (404 is returned as-is for callers to test)."""
    kw.setdefault("timeout", 30)
    for attempt in range(retries):
        try:
            r = _session.request(method, url, **kw)
        except requests.RequestException as e:
            log.debug("%s %s failed: %s", method, url, e)
            r = None
        if r is not None:
            if r.status_code in ok_status or r.status_code == 404:
                return r
            if r.status_code not in (403, 429, 500, 502, 503, 504):
                log.debug("%s %s -> %s", method, url, r.status_code)
                return None
            wait = float(r.headers.get("Retry-After") or backoff * (2 ** attempt))
        else:
            wait = backoff * (2 ** attempt)
        time.sleep(min(wait, 60))
    return None


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def today() -> str:
    return now_utc().strftime("%Y-%m-%d")


def parse_date(s: str) -> datetime:
    return datetime.strptime(s[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)


def months_between(start: str, end: datetime | None = None) -> float:
    end = end or now_utc()
    return max((end - parse_date(start)).days / 30.44, 0.0)


def window_start(months: int | None = None) -> str:
    months = months or CONFIG["window_months"]
    return (now_utc() - timedelta(days=int(months * 30.44))).strftime("%Y-%m-%d")


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def gh_token_headers() -> dict:
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    h = {"Accept": "application/vnd.github+json"}
    if tok:
        h["Authorization"] = f"Bearer {tok}"
    return h
