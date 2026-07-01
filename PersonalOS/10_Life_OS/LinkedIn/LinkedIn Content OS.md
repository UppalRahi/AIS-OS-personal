# LinkedIn Content OS

Personal branding for Rahi's LinkedIn. **Refined notes only** — no scripts, JSON, or raw scrape data here.

## How to create a post

Say **`/linkedin-content`** or "help me write a LinkedIn post."

The agent runs the [[content-intake-form]] — asks 7 questions, you answer in your own words, it refines slightly and returns a draft.

You review. You edit. You post manually.

## What's in this folder

| File | Purpose |
|------|---------|
| [[content-intake-form]] | Questions the agent asks every time |
| `references/` | Frameworks and voice rules (read-only context) |
| `drafts/` | Approved-ready post drafts (markdown only) |

## Voice (short version)

- Not salesy. Not flexing client work.
- Your inner voice: observant, humble, useful to GTM people.
- Expertise through clarity, not credentials.

Full rules: `references/voice-guardrails.md`

## Positioning

GTM systems thinking for people who run outbound, enrichment, and ops — from an engineer who removes friction quietly.

## Related

- [[10_Life_OS/Career & Education]]
- [[10_Life_OS/Vision & Values]]
- [[40_Resources/n8n Playbook]]

## Agent tooling (outside PersonalOS)

Scrape scripts and creator research data live in `.claude/skills/linkedin-content/data/`. The agent uses that internally; you don't need to open it.
