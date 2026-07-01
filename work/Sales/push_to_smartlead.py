#!/usr/bin/env python3
"""Upload claude_strong_fit leads to Smartlead campaign via API."""

import json
import os
import sys
import urllib.request
from pathlib import Path

CAMPAIGN_ID = 3569858
PAYLOAD = Path(__file__).parent / "claude_strong_fit_upload_payload.json"
ENV_FILE = Path(__file__).parent / ".env"


def load_api_key() -> str:
    key = os.environ.get("SMARTLEAD_API_KEY", "").strip()
    if key:
        return key
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            if k.strip() == "SMARTLEAD_API_KEY":
                return v.strip().strip('"').strip("'")
    return ""


def upload_batch(campaign_id: int, api_key: str, lead_list: list, settings: dict) -> dict:
    url = f"https://api.smartlead.ai/v1/campaigns/{campaign_id}/leads-v2?api_key={api_key}"
    payload = {"lead_list": lead_list, "settings": settings}
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    api_key = load_api_key()
    if not api_key:
        print("SMARTLEAD_API_KEY not set. Add to env or work/Sales/.env")
        sys.exit(1)

    data = json.loads(PAYLOAD.read_text(encoding="utf-8"))
    leads = data["lead_list"]
    settings = data.get("settings", {})

    print(f"Uploading {len(leads)} leads to campaign {CAMPAIGN_ID}...")
    # Single batch (under 1000 limit)
    result = upload_batch(CAMPAIGN_ID, api_key, leads, settings)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
