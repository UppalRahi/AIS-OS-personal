#!/usr/bin/env python3
"""Analyze scraped LinkedIn posts and write analysis_summary.json."""

from __future__ import annotations

import argparse
import json
import statistics
import re
from collections import Counter
from pathlib import Path
from typing import Any


def hook_pattern(hook: str) -> str:
    if any(c.isdigit() for c in hook[:30]):
        return "number_led"
    if "?" in hook[:100]:
        return "question"
    h = hook.lower()
    if any(w in h for w in ["i ", "my ", "we ", "our "]):
        return "first_person"
    if any(w in h for w in ["how ", "why ", "what "]):
        return "how_why_what"
    return "statement"


def analyze_profile(posts_path: Path, profile_path: Path) -> dict[str, Any]:
    posts = json.loads(posts_path.read_text())
    profile = json.loads(profile_path.read_text())
    originals = [p for p in posts if not p.get("is_repost")]

    by_type = Counter(p["content_type"] for p in originals)
    hook_patterns = Counter(hook_pattern(p.get("hook", "")) for p in originals)

    def top_n(key: str, n: int = 10) -> list[dict[str, Any]]:
        return sorted(originals, key=lambda x: x.get(key) or 0, reverse=True)[:n]

    top = top_n("engagement_total")
    return {
        "profile": profile,
        "total_posts": len(posts),
        "original_posts": len(originals),
        "repost_pct": round((len(posts) - len(originals)) / len(posts) * 100, 1) if posts else 0,
        "content_mix": dict(by_type.most_common()),
        "avg_char_count": round(statistics.mean([p["char_count"] for p in originals])) if originals else 0,
        "avg_line_count": round(statistics.mean([p["line_count"] for p in originals]), 1) if originals else 0,
        "avg_engagement": round(statistics.mean([p["engagement_total"] for p in originals]), 1) if originals else 0,
        "media_pct": round(sum(1 for p in originals if p.get("has_media")) / len(originals) * 100, 1) if originals else 0,
        "hook_patterns": dict(hook_patterns.most_common()),
        "top_posts": [
            {
                "hook": p["hook"][:150],
                "engagement": p["engagement_total"],
                "reactions": p["reactions"],
                "comments": p["comments"],
                "type": p["content_type"],
                "posted_at": p["posted_at"],
                "char_count": p["char_count"],
                "share_url": p.get("share_url"),
            }
            for p in top
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dir",
        type=Path,
        default=Path(".claude/skills/linkedin-content/data/profiles"),
        help="Directory with scraped profile data",
    )
    parser.add_argument("--slug", action="append", help="Profile slug(s) to analyze; default all in registry")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    data_dir = args.dir if args.dir.is_absolute() else repo_root / args.dir

    slugs = args.slug or []
    if not slugs:
        registry = data_dir / "registry.json"
        if registry.exists():
            slugs = [c["public_identifier"] for c in json.loads(registry.read_text()).get("creators", [])]
        else:
            slugs = [p.name.replace("_posts.json", "") for p in data_dir.glob("*_posts.json")]

    results = {}
    for slug in slugs:
        posts_path = data_dir / f"{slug}_posts.json"
        profile_path = data_dir / f"{slug}_profile.json"
        if posts_path.exists() and profile_path.exists():
            results[slug] = analyze_profile(posts_path, profile_path)

    out = data_dir / "analysis_summary.json"
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"Wrote {out} ({len(results)} profiles)")


if __name__ == "__main__":
    main()
