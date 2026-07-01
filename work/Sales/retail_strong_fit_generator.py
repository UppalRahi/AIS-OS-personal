#!/usr/bin/env python3
"""
Retail Strong Fit Campaign — AI-personalized 2-step email generator

References:
  - work/Anshuls_voice_skill.md
  - PersonalOS/40_Resources/GTM Brainstorming/Amply Retail Outreach Plays.md
  - PersonalOS/40_Resources/GTM Brainstorming/README.md (GTM Engineering framework)
  - conf_retail_US_similar_regions (best reply-rate Smartlead sequence)

Set your API key:
  cp .env.example .env   # then add OPENAI_API_KEY=sk-... to .env
  # or: export OPENAI_API_KEY="sk-..."

Usage:
  python3 retail_strong_fit_generator.py
  python3 retail_strong_fit_generator.py --preview --limit 3
  python3 retail_strong_fit_generator.py --no-ai          # rule-based fallback only
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent

INPUT_CSV = SCRIPT_DIR / "Retail-Operations-Leadership,-Various-Sectors-Default-view-export-1782816888611.csv"
OUTPUT_CSV = SCRIPT_DIR / "claude_strong_fit_leads.csv"
OUTPUT_JSON = SCRIPT_DIR / "claude_strong_fit_leads.json"
ENV_FILE = SCRIPT_DIR / ".env"

REFERENCE_FILES = {
    "anshul_voice": REPO_ROOT / "work" / "Anshuls_voice_skill.md",
    "amply_retail_plays": REPO_ROOT / "PersonalOS" / "40_Resources" / "GTM Brainstorming" / "Amply Retail Outreach Plays.md",
    "gtm_framework": REPO_ROOT / "PersonalOS" / "40_Resources" / "GTM Brainstorming" / "README.md",
}

# Best-performing US retail cold sequence (conf_retail_US_similar_regions, Smartlead)
WINNING_REPLY_EMAILS = """
### Email 1 (highest reply rate — expansion + visibility gap hook)
Subject pattern: {Automate|Move|Bring|Digitise} {{company_name}}'s store tasks + {comms|communication} + {area visits|store visits} into {an|one} app

Hi {{first_name}}, just hopping on here from our interaction on Linkedin.

We have yet to be properly introduced but I'm Anshul and am the CEO of Amply. My team saw {{LI_first_name}}'s post on the {{email_place}} store opening and couldn't stop talking about your growth at {{company_name}} yesterday.

At your scale, just curious how do your district leaders see a roll-up of store-wise completion rate on daily store tasks, RM store visit reports, store opening/closing checklists.

If you're anything like Hibbett, Webster, Mango before they found us — your field teams are trying to manage their tasks and communication on excel & email chains.

With Amply, you can set daily task schedules for your stores + broadcast comms + get alerts if SOP compliance drops at any store. Store managers can go look at their tasks, merchandising missions, weekly to-do list at one place.

Do you think such a tool could help you align all locations for a consistent store experience and boost your sales?

Happy to set a 30-min demo for you next week if worth a look — just let me know what time works, and I'll send an invite.

Cheers,
Anshul

### Email 2 (soft nudge follow-up — 10 day delay, threads on Email 1)
Hi {{first_name}},

My name might look familiar from our interaction on Linkedin. This will just take 30 sec - thought it made sense to just reach out once more and check if :

- your RMs are still recording store visit reports on paper/excel
- your VM team's going through thousands of images manually
- your Store Managers have no single view of their daily tasks

If any of the above is true, we'd love to show you how Hibbett, Footlocker, Mango use our mobile-first solution for their store task management + communications + VM executions.

{{company_name}}'s {{email_place}} store openings made me reach out, since SOPs start becoming crucial for consistent store experience at your scale.

I totally understand if you're too busy to respond. Even a one or two line reply will completely make my day.

All the best,
Anshul

P.S. we offer a 15-day free pilot run on your own checklists + app training for your field team
"""

OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")


# ---------------------------------------------------------------------------
# API key
# ---------------------------------------------------------------------------
def load_api_key() -> str | None:
    """Load OPENAI_API_KEY from env or work/Sales/.env (KEY=value lines)."""
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if key:
        return key
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            if k.strip() == "OPENAI_API_KEY":
                return v.strip().strip('"').strip("'")
    return None


def require_api_key(no_ai: bool) -> str | None:
    if no_ai:
        return None
    key = load_api_key()
    if not key or key in ("sk-...", "your-openai-api-key-here", "YOUR_OPENAI_API_KEY"):
        print(
            "\n[ERROR] OPENAI_API_KEY not set.\n"
            "  export OPENAI_API_KEY='sk-...'\n"
            f"  or create {ENV_FILE} with:\n"
            "  OPENAI_API_KEY=sk-...\n"
        )
        sys.exit(1)
    return key


# ---------------------------------------------------------------------------
# Reference context loader
# ---------------------------------------------------------------------------
def load_reference_context(max_chars_per_file: int = 12000) -> str:
    """Load GTM + Anshul voice files for the system prompt."""
    chunks = [f"## Winning reply emails (Smartlead benchmark)\n{WINNING_REPLY_EMAILS}"]

    for label, path in REFERENCE_FILES.items():
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="ignore")[:max_chars_per_file]
            chunks.append(f"## {label} ({path.name})\n{text}")
        else:
            chunks.append(f"## {label}\n[file not found: {path}]")

    return "\n\n---\n\n".join(chunks)


# ---------------------------------------------------------------------------
# Signal extraction from CSV row
# ---------------------------------------------------------------------------
def clean_company(name: str) -> str:
    if not name:
        return ""
    name = re.sub(r"\([^)]*\)", "", name).strip()
    for pat in [r"\binc\b\.?", r"\bllc\b\.?", r"\bco\b\.?", r"\bltd\b\.?", r"\bcorp\b\.?"]:
        name = re.sub(pat, "", name, flags=re.I).strip()
    name = re.sub(r"\s+", " ", name).strip(" ,.-")
    if name.isupper() and len(name) > 3:
        name = name.title()
    return name


def extract_store_count(reason: str) -> str:
    if not reason:
        return "20+"
    patterns = [
        r"(\d+)\+?\s*(?:store|location|brick-and-mortar|boutique)",
        r"over\s+(\d+)",
        r"(\d+)\s+locations",
        r"(\d+)\s+physical\s+store",
        r"lists?\s+(\d+)",
        r"had\s+(\d+)",
        r"operates?\s+(\d+)",
    ]
    for pat in patterns:
        m = re.search(pat, reason, re.I)
        if m:
            return m.group(1)
    return "20+"


def extract_opening_hook(openings_reason: str, expansion_reason: str) -> tuple[str, str]:
    text = (openings_reason or "") + " " + (expansion_reason or "")
    city_match = re.search(r"(?:in|at|for)\s+([A-Z][a-zA-Z\s]+(?:,\s*[A-Z]{2})?)", text)
    city = city_match.group(1).strip() if city_match else ""
    if not city:
        city_match = re.search(r"([A-Z][a-z]+(?:,\s*[A-Z]{2})?)\s+(?:store|location|opening)", text)
        city = city_match.group(1).strip() if city_match else ""

    detail = ""
    if openings_reason:
        first_sentence = openings_reason.split(".")[0].strip()
        if len(first_sentence) > 20:
            detail = first_sentence
    if not detail and expansion_reason:
        detail = expansion_reason.split(".")[0].strip()
    return city, detail


def classify_signals(row: dict) -> dict:
    """Build structured account signals for the AI prompt."""
    company_raw = (row.get("Company Table Data") or "").strip()
    company = clean_company(company_raw)
    job_title = (row.get("Job Title") or "").strip()
    headline = (row.get("Headline") or "").strip()
    summary = (row.get("Summary") or "").strip()
    description = (row.get("Description") or "").strip()

    store_count_reason = row.get("Estimated Store Count Reason") or ""
    digital_ops_reason = row.get("Uses Digital Operations Tool Reason") or ""
    expansion_reason = row.get("Funding Or Expansion Activity Reason") or ""
    openings_reason = row.get("Recent Or Upcoming Store Openings Reason") or ""

    store_count = extract_store_count(store_count_reason)
    city, opening_detail = extract_opening_hook(openings_reason, expansion_reason)
    no_digital_ops = "no evidence" in digital_ops_reason.lower()

    signals = []
    if opening_detail:
        signals.append(f"RETAIL_EXPANSION: {opening_detail}")
    if expansion_reason and expansion_reason not in opening_detail:
        signals.append(f"FUNDING_OR_GROWTH: {expansion_reason[:300]}")
    if no_digital_ops:
        signals.append("NO_DIGITAL_OPS_TOOL: likely paper/Excel/WhatsApp for store tasks")
    if store_count_reason:
        signals.append(f"STORE_FOOTPRINT: ~{store_count} locations — {store_count_reason[:200]}")
    if "visual merchandis" in (headline + summary + job_title).lower():
        signals.append("VM_FOCUS: leader cares about visual merchandising / display compliance")
    if any(x in job_title.lower() for x in ["coo", "chief operating", "vp of retail", "director of retail", "head of store"]):
        signals.append("SENIOR_OPS_BUYER: direct store ops decision-maker")

    # Map to Amply GTM plays (from Amply Retail Outreach Plays.md)
    recommended_plays = []
    if opening_detail or "expand" in expansion_reason.lower():
        recommended_plays.append("Play 2: Visual Merchandising Expansion Trigger (new stores / coming soon)")
    if no_digital_ops:
        recommended_plays.append("Play 3: Manual SOP Coordinator (paper/Excel/WhatsApp friction)")
    recommended_plays.append("Campaign 2 Option 1: Excel & WhatsApp Lag (PQS)")
    recommended_plays.append("Campaign 2 Option 2: Leadership Visibility Gap (PQS)")

    return {
        "first_name": (row.get("First Name") or "").strip() or "there",
        "last_name": (row.get("Last Name") or "").strip(),
        "email": (row.get("Work Email") or "").strip(),
        "company": company,
        "company_raw": company_raw,
        "job_title": job_title,
        "headline": headline,
        "summary": summary[:500] if summary else "",
        "location": (row.get("Location") or "").strip(),
        "linkedin": (row.get("LinkedIn Profile") or "").strip(),
        "domain": (row.get("Company Domain") or "").strip(),
        "store_count": store_count,
        "expansion_city": city,
        "opening_detail": opening_detail,
        "no_digital_ops": no_digital_ops,
        "signals": signals,
        "recommended_plays": recommended_plays,
        "description_excerpt": description[:400] if description else "",
    }


# ---------------------------------------------------------------------------
# OpenAI generation
# ---------------------------------------------------------------------------
def generate_with_openai(api_key: str, signals: dict, reference_context: str) -> dict | None:
    """Call OpenAI to draft personalized 2-step sequence. Returns parsed JSON or None."""
    system = f"""You are Anshul, Founder @ Amply (backed by Google), writing cold outbound to US retail ops leaders.

Follow GTM Engineering: lead with THE SITUATION (observable signal), not generic pitching.
Use Pain-Qualified Segment (PQS) framing — name their specific operational tension.
Write as Anshul: casual but professional, short sentences, no fluff, no "hope this finds you well".

REFERENCE MATERIAL (voice, plays, framework, winning emails):
{reference_context}

STRICT RULES:
- 2 emails only (email_1 + email_2 follow-up threading on email_1)
- Plain text bodies with \\n line breaks (no HTML)
- Email 1: under 150 words. Open with a signal-specific hook referencing THEIR data (store count, expansion, no digital ops tool, VM focus)
- Email 1 subject: use Anshul formula e.g. "Digitise {{company}}'s store tasks + comms + area visits into one app" OR "store SOP compliance at {{company}}" — pick best fit for signals
- Email 1 CTA: low-friction question OR offer 30-min demo next week
- Email 1 sign-off EXACTLY:
--
Anshul
Founder @ Amply (backed by Google)
+91 9706821560
- Email 2: under 120 words. Soft nudge. 3 bullet pain checks. Reference their expansion signal again. End with "Even a one or two line reply will completely make my day." + P.S. 15-day trial
- Proof brands (pick 2-3): Footlocker, Miniso, Mango, Levi's, Caratlane, ASICS — match US retail audience
- NEVER invent facts not in ACCOUNT SIGNALS. If unsure, ask a question instead.
- Use paper/excel/whatsapp pain shorthand when no_digital_ops is true
- Do NOT include links unless absolutely necessary (prefer none)

Output strict JSON:
{{
  "gtm_play": "expansion|manual_ops|vm|visibility_gap|whatsapp_lag",
  "play_name": "which Amply GTM play you applied",
  "email_1_subject": "...",
  "email_1_body": "...",
  "email_2_body": "..."
}}"""

    user = f"""Write a 2-step cold email sequence for this prospect.

ACCOUNT SIGNALS:
{json.dumps(signals, indent=2)}

Recommended GTM plays to consider: {', '.join(signals['recommended_plays'])}

Pick the strongest play based on signals. Personalize using store_count, opening_detail, expansion_city, job_title, headline, and no_digital_ops."""

    payload = {
        "model": OPENAI_MODEL,
        "response_format": {"type": "json_object"},
        "temperature": 0.45,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }

    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        content = data["choices"][0]["message"]["content"]
        return json.loads(content)
    except Exception as e:
        print(f"  [OpenAI error] {e}")
        return None


# ---------------------------------------------------------------------------
# Rule-based fallback (when --no-ai or API fails)
# ---------------------------------------------------------------------------
def generate_fallback(signals: dict) -> dict:
    first_name = signals["first_name"]
    company = signals["company"]
    store_count = signals["store_count"]
    opening_detail = signals["opening_detail"]
    city = signals["expansion_city"]
    no_digital_ops = signals["no_digital_ops"]
    job_title = signals["job_title"]
    headline = signals["headline"]

    title_lower = job_title.lower()
    headline_lower = headline.lower()

    if opening_detail and any(w in opening_detail.lower() for w in ["opening", "coming soon", "expand"]):
        gtm_play = "expansion"
        hook = f"I noticed {company} is pushing retail expansion"
        if city:
            hook += f" — including activity around {city}"
        hook += "."
    elif "visual merchandis" in headline_lower:
        gtm_play = "vm"
        hook = f"Given your focus on visual merchandising at {company}, scaling standards across {store_count} locations usually gets harder without real-time visibility."
    elif "coo" in title_lower or "chief operating" in title_lower:
        gtm_play = "ops_scale"
        hook = f"At {store_count} stores, {company}'s ops team usually starts losing visibility into daily SOP completion across regions."
    else:
        gtm_play = "manual_ops"
        hook = f"With {store_count} store locations, {company} is at the scale where daily checklist compliance usually slips unless ops is digitized."

    subject = f"Digitise {company}'s store tasks + comms + area visits into one app"

    pain_line = (
        f"From what we can tell, {company} doesn't appear to be on a dedicated store ops platform yet — so field teams may still be coordinating on paper, Excel, or WhatsApp."
        if no_digital_ops
        else "If you're anything like Footlocker, Miniso, and Caratlane before they found us — field teams are still trying to manage tasks and comms on Excel and email chains."
    )

    email_1_body = f"""Hi {first_name},

{hook}

At your scale, curious how your district leaders roll up store-wise completion on daily opening/closing checklists, area manager visit reports, and VM audits across {store_count} locations.

{pain_line}

With Amply, you can schedule daily store tasks, broadcast VM directives, and get alerts when SOP compliance drops at any location. Store managers see tasks, merchandising missions, and weekly to-dos in one mobile feed.

Do you think a tool like this could help {company} keep a consistent store experience as you scale?

Happy to set a 30-min demo next week if worth a look — just let me know what time works.

--
Anshul
Founder @ Amply (backed by Google)
+91 9706821560"""

    expansion_ref = opening_detail.split(".")[0] if opening_detail else f"{company}'s retail expansion"

    email_2_body = f"""Hi {first_name},

This will just take 15 sec — thought it made sense to reach out once more and check if:

- your area managers are recording store visits on paper/Excel?
- your VM team is going through thousands of audit images manually?
- store managers get daily tasks and comms in separate channels?

If any of the above is true, we'd love to show you how Footlocker, Miniso, and Mango use Amply for store task management + comms + VM executions.

{expansion_ref} made me reach out — daily compliance becomes crucial for consistent store experience at {store_count} locations.

I totally understand if you're too busy to respond. Even a one or two line reply will completely make my day.

All the best,
Anshul

P.S. we digitise your checklists for free and offer a 15-day trial with app training for your store managers."""

    return {
        "gtm_play": gtm_play,
        "play_name": "fallback_rule_based",
        "email_1_subject": subject,
        "email_1_body": email_1_body,
        "email_2_body": email_2_body,
    }


# ---------------------------------------------------------------------------
# Lead assembly
# ---------------------------------------------------------------------------
def build_lead(row: dict, emails: dict, signals: dict, source: str) -> dict:
    email = signals["email"]
    domain = signals["domain"] or email.split("@")[-1]
    return {
        "email": email,
        "first_name": signals["first_name"],
        "last_name": signals["last_name"],
        "company_name": signals["company"],
        "website": domain,
        "location": signals["location"],
        "linkedin_profile": signals["linkedin"],
        "custom_fields": {
            "job_title": signals["job_title"],
            "store_count": signals["store_count"],
            "gtm_play": emails.get("gtm_play", ""),
            "play_name": emails.get("play_name", ""),
            "generation_source": source,
            "email_1_subject": emails["email_1_subject"],
            "email_1_body": emails["email_1_body"],
            "email_2_body": emails["email_2_body"],
        },
    }


def load_cache() -> dict[str, dict]:
    """Resume: keyed by email -> flat row dict."""
    cache = {}
    if not OUTPUT_CSV.exists():
        return cache
    with open(OUTPUT_CSV, encoding="utf-8", errors="ignore") as f:
        for row in csv.DictReader(f):
            if row.get("email_1_body"):
                cache[row["email"].lower()] = row
    return cache


def should_regenerate(
    cached: dict | None,
    *,
    force: bool,
    api_key: str | None,
    index: int,
    ai_limit: int | None,
) -> bool:
    """Return True when we should call OpenAI/fallback instead of reusing CSV cache."""
    if force:
        return True
    if not cached:
        return True
    # --limit N is a test mode: always refresh first N leads with AI
    if api_key and ai_limit is not None and index <= ai_limit:
        return True
    # With API key, never reuse old rule-based rows — upgrade them to AI
    if api_key and cached.get("generation_source") != "openai":
        return True
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Generate AI-personalized retail strong-fit emails.")
    parser.add_argument("--preview", action="store_true", help="Print first N samples after generation")
    parser.add_argument("--limit", type=int, default=None, help="Test mode: regenerate first N leads with AI (ignores cache for those N)")
    parser.add_argument("--no-ai", action="store_true", help="Skip OpenAI; use rule-based fallback only")
    parser.add_argument("--force", action="store_true", help="Regenerate even if cached in output CSV")
    args = parser.parse_args()

    api_key = require_api_key(args.no_ai)
    reference_context = load_reference_context() if api_key else ""

    if not INPUT_CSV.exists():
        print(f"Error: input CSV not found at {INPUT_CSV}")
        sys.exit(1)

    with open(INPUT_CSV, encoding="utf-8", errors="ignore") as f:
        rows = list(csv.DictReader(f))

    cache = {} if args.force else load_cache()
    leads: list[dict] = []
    ai_count = 0
    fallback_count = 0
    cached_count = 0

    eligible = [r for r in rows if (r.get("Work Email") or "").strip()]
    total_eligible = len(eligible)
    ai_limit = args.limit

    stale_fallback = sum(
        1 for r in cache.values() if r.get("generation_source") != "openai"
    )
    if api_key and stale_fallback and not args.force:
        print(
            f"Note: {stale_fallback} leads in cache are rule-based fallback — "
            f"will regenerate with AI (or use --force to refresh all)."
        )

    print(f"Processing {total_eligible} leads ({len(rows) - total_eligible} skipped — no email)")
    if api_key:
        limit_note = f" (AI capped at first {ai_limit})" if ai_limit else ""
        print(f"Model: {OPENAI_MODEL}{limit_note} | References: GTM Brainstorming + Anshul voice skill")
    else:
        print("Mode: rule-based fallback (--no-ai)")

    for i, row in enumerate(eligible, 1):
        signals = classify_signals(row)
        email_key = signals["email"].lower()
        cached = cache.get(email_key)
        use_ai = api_key and (ai_limit is None or i <= ai_limit)

        if not should_regenerate(
            cached, force=args.force, api_key=api_key, index=i, ai_limit=ai_limit
        ):
            emails = {
                "gtm_play": cached.get("gtm_play", ""),
                "play_name": cached.get("play_name", "cached"),
                "email_1_subject": cached["email_1_subject"],
                "email_1_body": cached["email_1_body"],
                "email_2_body": cached["email_2_body"],
            }
            source = cached.get("generation_source", "cached")
            cached_count += 1
            print(f"  [{i}/{total_eligible}] {signals['first_name']} @ {signals['company']} — cached (openai)")
        else:
            mode = "AI" if use_ai else "fallback"
            print(f"  [{i}/{total_eligible}] {signals['first_name']} @ {signals['company']} — {mode}...")
            emails = None
            source = "openai"

            if use_ai:
                emails = generate_with_openai(api_key, signals, reference_context)
                if emails:
                    ai_count += 1

            if not emails:
                emails = generate_fallback(signals)
                source = "fallback"
                fallback_count += 1

        leads.append(build_lead(row, emails, signals, source))

    # Remove duplicate merge block — all leads appended in loop above

    fieldnames = [
        "email", "first_name", "last_name", "company_name", "website", "location",
        "linkedin_profile", "job_title", "store_count", "gtm_play", "play_name",
        "generation_source", "email_1_subject", "email_1_body", "email_2_body",
    ]

    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for lead in leads:
            flat = {**{k: lead[k] for k in lead if k != "custom_fields"}, **lead["custom_fields"]}
            writer.writerow(flat)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(leads, f, indent=2)

    print(f"\nDone: {len(leads)} leads written")
    print(f"  AI: {ai_count} | Fallback: {fallback_count} | Cached: {cached_count}")
    print(f"  CSV:  {OUTPUT_CSV}")
    print(f"  JSON: {OUTPUT_JSON}")

    if args.preview:
        for j, lead in enumerate(leads[:3]):
            cf = lead["custom_fields"]
            print(f"\n{'='*60}\nLead {j+1}: {lead['first_name']} @ {lead['company_name']}")
            print(f"Play: {cf.get('play_name')} ({cf.get('gtm_play')}) | Source: {cf.get('generation_source')}")
            print(f"Subject: {cf['email_1_subject']}")
            print(cf["email_1_body"][:500] + ("..." if len(cf["email_1_body"]) > 500 else ""))


if __name__ == "__main__":
    main()
