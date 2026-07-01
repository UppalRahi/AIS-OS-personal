#!/usr/bin/env python3
"""Safely scrape LinkedIn posts via Unipile API with rate limiting."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DEFAULT_BASE_URL = "https://api21.unipile.com:15191/api/v1"
REQUEST_DELAY_SEC = 2.5
MAX_LIMIT = 100


def env(name: str, default: str | None = None) -> str:
    value = os.environ.get(name, default)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


def api_get(path: str, params: dict[str, Any]) -> dict[str, Any]:
    base = env("UNIPILE_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
    api_key = env("UNIPILE_API_KEY")
    query = urlencode({k: v for k, v in params.items() if v is not None})
    url = f"{base}{path}?{query}" if query else f"{base}{path}"
    req = Request(url, headers={"X-API-KEY": api_key, "Accept": "application/json"})
    try:
        with urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise SystemExit(f"Unipile API error {exc.code}: {body}") from exc


def get_profile(public_id: str, account_id: str) -> dict[str, Any]:
    return api_get(f"/users/{public_id}", {"account_id": account_id, "notify": "false"})


def list_posts(identifier: str, account_id: str, cursor: str | None = None) -> dict[str, Any]:
    params: dict[str, Any] = {"account_id": account_id, "limit": MAX_LIMIT}
    if cursor:
        params["cursor"] = cursor
    return api_get(f"/users/{identifier}/posts", params)


def parse_post_date(post: dict[str, Any]) -> datetime | None:
    raw = post.get("parsed_datetime") or post.get("date")
    if not raw:
        return None
    try:
        if raw.endswith("Z"):
            return datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def classify_post(text: str, attachments: list[dict[str, Any]], is_repost: bool) -> str:
    if is_repost:
        return "repost"
    lower = (text or "").lower()
    if any(a.get("type") == "linkedin_post" for a in attachments or []):
        return "carousel_or_document"
    if re.search(r"\b(here('s| is) what|step \d|framework|playbook|template)\b", lower):
        return "educational_framework"
    if re.search(r"\b(client|saved|hours|revenue|\$|case study|results)\b", lower):
        return "proof_case_study"
    if re.search(r"\b(i |my |journey|learned|mistake|failed)\b", lower):
        return "personal_story"
    if re.search(r"\b(comment|dm|link|download|free|newsletter)\b", lower):
        return "lead_magnet_cta"
    return "thought_leadership"


def extract_hook(text: str) -> str:
    if not text:
        return ""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return lines[0][:200] if lines else text[:200]


def normalize_post(post: dict[str, Any], profile_meta: dict[str, Any]) -> dict[str, Any]:
    attachments = post.get("attachments") or []
    attachment_types = sorted({a.get("type") for a in attachments if a.get("type")})
    text = post.get("text") or ""
    is_repost = bool(post.get("is_repost"))
    reactions = int(post.get("reaction_counter") or 0)
    comments = int(post.get("comment_counter") or 0)
    reposts = int(post.get("repost_counter") or 0)
    impressions = post.get("impressions_counter")
    engagement = reactions + comments + reposts

    return {
        "post_id": post.get("id"),
        "social_id": post.get("social_id"),
        "share_url": post.get("share_url"),
        "posted_at": post.get("parsed_datetime") or post.get("date"),
        "text": text,
        "hook": extract_hook(text),
        "char_count": len(text),
        "line_count": len([ln for ln in text.splitlines() if ln.strip()]),
        "is_repost": is_repost,
        "content_type": classify_post(text, attachments, is_repost),
        "attachment_types": attachment_types,
        "has_media": bool(attachments),
        "reactions": reactions,
        "comments": comments,
        "reposts": reposts,
        "impressions": impressions,
        "engagement_total": engagement,
        "engagement_rate": round(engagement / impressions, 4) if impressions else None,
        "author_public_id": profile_meta.get("public_identifier"),
        "author_name": f"{profile_meta.get('first_name', '')} {profile_meta.get('last_name', '')}".strip(),
        "author_headline": profile_meta.get("headline"),
    }


def scrape_profile(
    public_id: str,
    account_id: str,
    months: int,
    delay_sec: float,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    profile = get_profile(public_id, account_id)
    time.sleep(delay_sec)

    cutoff = datetime.now(timezone.utc) - timedelta(days=months * 30)
    identifier = profile.get("provider_id") or public_id

    posts: list[dict[str, Any]] = []
    cursor: str | None = None
    page = 0

    while True:
        page += 1
        payload = list_posts(identifier, account_id, cursor)
        items = payload.get("items") or []
        if not items:
            break

        stop = False
        for item in items:
            posted = parse_post_date(item)
            if posted and posted < cutoff:
                stop = True
                continue
            posts.append(normalize_post(item, profile))

        cursor = payload.get("cursor")
        if stop or not cursor:
            break
        time.sleep(delay_sec)

    profile_meta = {
        "public_identifier": profile.get("public_identifier") or public_id,
        "provider_id": profile.get("provider_id"),
        "name": f"{profile.get('first_name', '')} {profile.get('last_name', '')}".strip(),
        "headline": profile.get("headline"),
        "follower_count": profile.get("follower_count"),
        "connections_count": profile.get("connections_count"),
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "months_window": months,
        "post_count": len(posts),
    }
    return profile_meta, posts


def write_outputs(out_dir: Path, profile_meta: dict[str, Any], posts: list[dict[str, Any]]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = profile_meta["public_identifier"]

    with open(out_dir / f"{slug}_profile.json", "w", encoding="utf-8") as f:
        json.dump(profile_meta, f, indent=2, ensure_ascii=False)

    with open(out_dir / f"{slug}_posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    if posts:
        fieldnames = list(posts[0].keys())
        with open(out_dir / f"{slug}_posts.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape LinkedIn posts via Unipile")
    parser.add_argument("profiles", nargs="+", help="LinkedIn public identifiers (e.g. vikashyavansh)")
    parser.add_argument("--months", type=int, default=12, help="Months of history to keep")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path(".claude/skills/linkedin-content/data/profiles"),
        help="Output directory (relative to repo root or absolute)",
    )
    parser.add_argument("--delay", type=float, default=REQUEST_DELAY_SEC, help="Delay between API calls")
    args = parser.parse_args()

    account_id = env("UNIPILE_ACCOUNT_ID")
    repo_root = Path(__file__).resolve().parents[4]
    out_dir = args.out_dir if args.out_dir.is_absolute() else repo_root / args.out_dir

    index: list[dict[str, Any]] = []
    for public_id in args.profiles:
        print(f"Scraping @{public_id} ...", file=sys.stderr)
        profile_meta, posts = scrape_profile(public_id, account_id, args.months, args.delay)
        write_outputs(out_dir, profile_meta, posts)
        index.append(profile_meta)
        print(f"  -> {len(posts)} posts saved", file=sys.stderr)
        time.sleep(args.delay)

    with open(out_dir / "index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(json.dumps({"profiles": index, "out_dir": str(out_dir)}, indent=2))


if __name__ == "__main__":
    main()
