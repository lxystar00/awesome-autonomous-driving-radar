"""Claude-based relevance check, topic, TL;DR and quality rubric.

Configuration (env):
  ANTHROPIC_API_KEY              API key (GitHub Actions secret)
  ANTHROPIC_BASE_URL             optional gateway
  ANTHROPIC_CUSTOM_HEADERS       optional "Name: value" lines, sent on every request
  AD_RADAR_MODEL / ANTHROPIC_DEFAULT_SONNET_MODEL   model override
If the API is unreachable the pipeline continues with heuristic scores only.
"""
from __future__ import annotations

import json
import os
import re

from common import CONFIG, log, now_utc

TOPICS = CONFIG["topics"]

SYSTEM = f"""You are a senior autonomous-driving researcher curating a high-precision reading list.
For each paper, return an object with:
- "id": the paper id, unchanged
- "relevant": true only if autonomous driving / driving scenes are a primary focus (not a passing mention)
- "topic": one of {list(TOPICS)}
- "tldr": one sentence, <= 30 words, concrete contribution and key result
- "tldr_zh": the same in Chinese, <= 50 characters
- "novelty", "rigor", "impact": integers 1-10. Be strict: 5 is an average arXiv paper, 8+ is top-venue oral quality, 10 is field-defining
- "sota": true if the abstract claims state-of-the-art on a named public benchmark
- "benchmarks": list of benchmark names used (e.g. nuScenes, NAVSIM, Bench2Drive, Waymo Open, CARLA)
- "orgs": list of notable institutions or companies you can infer (empty if unknown; do not guess)
Return ONLY a JSON array, no prose."""


def _client():
    try:
        import anthropic
    except ImportError:
        return None
    headers = {}
    for line in os.environ.get("ANTHROPIC_CUSTOM_HEADERS", "").splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip()] = v.strip()
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key and not os.environ.get("ANTHROPIC_BASE_URL"):
        return None
    return anthropic.Anthropic(
        api_key=key or "unused",
        base_url=os.environ.get("ANTHROPIC_BASE_URL") or None,
        default_headers=headers or None,
        max_retries=3,
        timeout=120,
    )


def model_name() -> str:
    return (os.environ.get("AD_RADAR_MODEL")
            or os.environ.get("ANTHROPIC_DEFAULT_SONNET_MODEL")
            or CONFIG["llm"]["default_model"])


def _parse(text: str) -> list[dict]:
    m = re.search(r"\[.*\]", text, re.S)
    return json.loads(m.group(0)) if m else []


def _prompt(batch: list[dict]) -> str:
    items = [{"id": p["id"], "title": p["title"], "abstract": p["abstract"][:2000],
              "comments": p.get("comments", "")[:300]} for p in batch]
    return json.dumps(items, ensure_ascii=False)


def score(papers: list[dict], limit: int | None = None) -> int:
    """Annotate papers lacking an LLM verdict in place. Returns number scored."""
    client = _client()
    if client is None:
        log.warning("LLM: no Anthropic credentials; skipping")
        return 0
    todo = [p for p in papers if "llm" not in p][: limit or CONFIG["llm"]["max_per_run"]]
    bs, done, model = CONFIG["llm"]["batch_size"], 0, model_name()
    log.info("LLM: scoring %d papers with %s", len(todo), model)
    for i in range(0, len(todo), bs):
        batch = todo[i:i + bs]
        try:
            msg = client.messages.create(
                model=model, max_tokens=4000, system=SYSTEM,
                messages=[{"role": "user", "content": _prompt(batch)}],
            )
            results = {r["id"]: r for r in _parse(msg.content[0].text) if isinstance(r, dict) and "id" in r}
        except Exception as e:  # network, quota, bad JSON: degrade gracefully
            log.warning("LLM batch failed (%s); stopping LLM scoring this run", str(e)[:200])
            break
        for p in batch:
            r = results.get(p["id"])
            if not r:
                continue
            q = [r.get(k) for k in ("novelty", "rigor", "impact")]
            q = [int(x) for x in q if isinstance(x, (int, float))]
            p["llm"] = {
                "relevant": bool(r.get("relevant", True)),
                "topic": r.get("topic") if r.get("topic") in TOPICS else None,
                "tldr": (r.get("tldr") or "").strip(),
                "tldr_zh": (r.get("tldr_zh") or "").strip(),
                "quality": round(sum(q) / len(q), 2) if q else None,
                "sota": bool(r.get("sota")),
                "benchmarks": r.get("benchmarks") or [],
                "orgs": r.get("orgs") or [],
                "model": model,
                "at": now_utc().strftime("%Y-%m-%d"),
            }
            done += 1
    log.info("LLM: scored %d papers", done)
    return done


def summarize_news(items: list[dict]) -> str | None:
    """Short Chinese+English digest of the day's company news (optional)."""
    client = _client()
    if client is None or not items:
        return None
    lines = "\n".join(f"- [{it['company']}] {it['title']} ({it['source']})" for it in items[:80])
    try:
        msg = client.messages.create(
            model=model_name(), max_tokens=1200,
            system="You summarize autonomous-driving industry news for engineers. Be factual, no hype.",
            messages=[{"role": "user", "content":
                       "Write 3-6 bullet points summarizing the most important developments below "
                       "(product launches, robotaxi deployments, regulation, research/open-source releases). "
                       "Skip stock/market chatter. English first line, then Chinese translation per bullet.\n\n" + lines}],
        )
        return msg.content[0].text.strip()
    except Exception as e:
        log.warning("LLM news summary failed: %s", str(e)[:200])
        return None
