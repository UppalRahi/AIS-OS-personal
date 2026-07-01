---
name: linkedin-content
description: >-
  Runs a 7-question intake interview for Rahi's LinkedIn posts, refines raw answers
  lightly using Lara Acosta SLAY and voice guardrails, saves drafts to PersonalOS.
  Use when the user wants to write a LinkedIn post, says /linkedin-content, or asks
  to publish content on LinkedIn. Never generates from scratch without intake answers.
---

# LinkedIn Content — Intake & Refine

Rahi provides **raw input**. You **ask questions**, **refine slightly**, **return draft for approval**.

PersonalOS holds refined markdown only: `PersonalOS/10_Life_OS/LinkedIn/`

## Trigger

User says: `/linkedin-content`, "write a LinkedIn post", "help me publish on LinkedIn", or similar.

**Do not** draft a post until intake is complete — unless user pastes full raw draft and says "just clean this up."

## Phase 1 — Intake interview (mandatory)

Read `PersonalOS/10_Life_OS/LinkedIn/content-intake-form.md` and ask all 7 questions.

Use **AskQuestion** for Q5 and Q7 (multiple choice). Ask Q1–Q4 and Q6 conversationally as open text.

| # | Question |
|---|----------|
| 1 | What triggered this post? |
| 2 | What were you doing when you noticed it? |
| 3 | What surprised you or felt wrong? |
| 4 | What would actually help someone in GTM? |
| 5 | How personal? (observation / light / reflective) |
| 6 | Opening line (optional — their words or blank) |
| 7 | How should it end? (question / quiet close / still figuring out) |

Wait for answers. If user gives partial answers, ask only what's missing.

## Phase 2 — Refine (light touch)

Read before refining:
- `PersonalOS/10_Life_OS/LinkedIn/references/voice-guardrails.md`
- `PersonalOS/10_Life_OS/LinkedIn/references/reference-acosta-framework.md`
- `references/voice.md` (repo root)

**Refine rules:**
- Keep **80%+ of user's words, ideas, and tone**
- Short lines. One thought per line. Mobile skim.
- Remove salesy/flex language even if user included it
- No invented client results or metrics
- No em dashes
- End per Q7 — default to open question, never "DM me"

**Do not:** rewrite into guru voice, add tool-stack lists, or turn into case study unless user explicitly asked.

Output format:

```markdown
## LinkedIn Draft — [TITLE]
**Intake date:** YYYY-MM-DD | **Tone:** [observation/light/reflective]

[POST BODY — ready to copy]

---
**Changed from your raw input:** [1-2 bullets only if you cut or reordered something meaningful]
**Your call:** edit anything that doesn't sound like you, then post.
```

## Phase 3 — Save (after user approves or requests save)

Write to `PersonalOS/10_Life_OS/LinkedIn/drafts/YYYY-MM-DD-slug.md` with post body + metadata.

Only save when user says to save, or after they approve the draft.

## PersonalOS vs agent tooling

| Location | Contains |
|----------|----------|
| `PersonalOS/10_Life_OS/LinkedIn/` | Intake form, voice refs, frameworks, **drafts** — markdown only |
| `.claude/skills/linkedin-content/data/` | Scraped profiles (JSON/CSV) — agent research, not vault |
| `.claude/skills/linkedin-content/scripts/` | Scrape/analyze scripts — not in PersonalOS |

See `PersonalOS/00_System/references/personalos-vault-rules.md`.

## Optional: creator research (agent-only)

If user asks to scrape or analyze a LinkedIn creator:

```bash
python3 .claude/skills/linkedin-content/scripts/scrape_profile_posts.py SLUG --months 12
python3 .claude/skills/linkedin-content/scripts/analyze_posts.py
```

Summarize insights into a **new refined note** in `references/` only if user wants it saved to vault. Never dump JSON into PersonalOS.

## Additional refs

- `PersonalOS/10_Life_OS/LinkedIn/references/reference-rahi-angles.md` — topic pillars
- `PersonalOS/10_Life_OS/LinkedIn/references/reference-acosta-framework.md` — SLAY structure
- `PersonalOS/10_Life_OS/LinkedIn/references/reference-swipe-analysis.md` — what works in GTM niche (structure only)
