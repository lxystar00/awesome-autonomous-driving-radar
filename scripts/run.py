"""AD Radar pipeline.

  python scripts/run.py                         # daily: harvest since last run, news, render
  python scripts/run.py --backfill 2025-09-25   # harvest everything submitted since a date
  python scripts/run.py --weekly                # also write weekly/YYYY-Www.md
  python scripts/run.py --no-llm --no-news      # offline-ish run
"""
from __future__ import annotations

import argparse
import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import arxiv_fetch  # noqa: E402
import enrich  # noqa: E402
import llm  # noqa: E402
import news as news_mod  # noqa: E402
import rank  # noqa: E402
import render  # noqa: E402
from common import CONFIG, DATA, load_json, log, now_utc, save_json, setup_logging, today, window_start  # noqa: E402

PAPERS = DATA / "papers.json"
NEWS = DATA / "news.json"
STATE = DATA / "state.json"
CURATED = DATA / "curated.json"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backfill", metavar="YYYY-MM-DD", help="harvest papers submitted since this date")
    ap.add_argument("--until", metavar="YYYY-MM-DD", help="with --backfill: stop harvesting at this date")
    ap.add_argument("--weekly", action="store_true")
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--no-news", action="store_true")
    ap.add_argument("--no-harvest", action="store_true", help="skip arXiv, re-rank stored papers only")
    ap.add_argument("--llm-limit", type=int, default=None)
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()
    setup_logging(args.verbose)

    papers: dict[str, dict] = load_json(PAPERS, {})
    state = load_json(STATE, {})
    win = window_start()
    date = today()

    # 1. Harvest arXiv.
    new_ids: list[str] = []
    if not args.no_harvest:
        if args.backfill:
            since, created_after = args.backfill, args.backfill
        else:
            last = state.get("last_harvest") or (now_utc() - timedelta(days=3)).strftime("%Y-%m-%d")
            since, created_after = last, win
        for p in arxiv_fetch.fetch(since, args.until or date, created_after=created_after):
            old = papers.get(p["id"])
            if old is None:
                p["first_seen"] = date
                papers[p["id"]] = p
                new_ids.append(p["id"])
            else:
                keep_code = old.get("code_url")
                old.update({k: v for k, v in p.items() if k != "code_url"})
                old["code_url"] = keep_code or p["code_url"]
        if not args.until:
            state["last_harvest"] = date
        log.info("papers: %d new, %d total", len(new_ids), len(papers))

    # Drop papers that fell out of the window (keep a small grace period).
    grace = (now_utc() - timedelta(days=int(CONFIG["window_months"] * 30.44) + 31)).strftime("%Y-%m-%d")
    for pid in [k for k, v in papers.items() if v["published"] < grace]:
        del papers[pid]
    active = [p for p in papers.values() if p["published"] >= win]

    # 2. Enrich with external signals.
    enrich.enrich_s2(active)
    enrich.enrich_hf(active)
    for p in active:
        enrich.compute_signals(p)
        p["topic"] = rank.topic(p)
        p["score"] = rank.score(p)
    enrich.enrich_github(active, CONFIG["github"]["max_requests_per_run"], CONFIG["github"]["refresh_days"])

    # 3. LLM on the plausible candidates (new papers first, then best-scored).
    if not args.no_llm:
        limit = args.llm_limit or CONFIG["llm"]["max_per_run"]
        for p in active:
            p["score"] = rank.score(p)
        cands = rank.llm_candidates(active, limit)
        llm.score(cands, limit)

    for p in active:
        enrich.compute_signals(p)
        p["score"] = rank.score(p)
    enrich.discover_code(active, CONFIG["github"]["max_searches_per_run"])
    for p in active:
        enrich.compute_signals(p)
        p["topic"] = rank.topic(p)
        p["score"] = rank.score(p)

    # 4. Curate.
    curated = rank.curate(active, win)
    log.info("curated: %d papers (eligible pool %d)", len(curated), sum(rank.eligible(p) for p in active))

    # 5. News.
    news_store: dict = load_json(NEWS, {})
    added_news: list[dict] = []
    if not args.no_news:
        added_news = news_mod.merge(news_store, news_mod.fetch(days=2 if not args.backfill else 14))
        log.info("news: %d new items", len(added_news))

    # 6. Render.
    stats = {"tracked": len(active)}
    render.write("README.md", render.readme(curated, stats, news_store))
    # Revised old papers show up in the harvest too; the digest only lists fresh ones.
    fresh = (now_utc() - timedelta(days=7)).strftime("%Y-%m-%d")
    new_papers = [papers[i] for i in new_ids if papers[i]["published"] >= fresh]
    if not args.backfill and (new_papers or added_news):
        summary = None if args.no_llm else llm.summarize_news(added_news)
        render.write(f"daily/{date}.md", render.daily(date, new_papers, added_news, summary))
    if args.weekly:
        d = now_utc()
        wk = f"{d.isocalendar().year}-W{d.isocalendar().week:02d}"
        wk_start = (d - timedelta(days=7)).strftime("%Y-%m-%d")
        wk_papers = [p for p in active if p.get("first_seen", "") >= wk_start and p["published"] >= wk_start]
        wk_news = [n for n in news_store.values() if n["date"] >= wk_start]
        summary = None if args.no_llm else llm.summarize_news(wk_news)
        render.write(f"weekly/{wk}.md", render.weekly(wk, wk_papers, wk_news, summary))

    save_json(PAPERS, papers)
    save_json(NEWS, news_store)
    save_json(STATE, state)
    save_json(CURATED, [{k: p.get(k) for k in ("id", "title", "url", "code_url", "stars", "venue", "published",
                                                "citations", "topic", "score")} for p in curated])
    log.info("done")


if __name__ == "__main__":
    main()
