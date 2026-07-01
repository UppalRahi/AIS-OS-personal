# PersonalOS Vault Rules

Conventions for what belongs inside `PersonalOS/` vs outside.

## PersonalOS is for refined knowledge

Only store **markdown files worth re-reading** — notes, frameworks, drafts, decisions, client summaries.

| Belongs in PersonalOS | Does NOT belong in PersonalOS |
|-----------------------|-------------------------------|
| Voice guardrails, frameworks | Python/Bash scripts |
| Post drafts (`.md`) | JSON/CSV data dumps |
| Intake forms, SOPs | Scrape outputs, API payloads |
| Client/project notes | Generated images (unless archived deliberately) |
| Templates | `node_modules`, `.env`, credentials |

**Rule:** If it's raw machine output or executable tooling, put it in `.claude/skills/`, `scripts/`, or `work/` — then distill insights back into PersonalOS as a short `.md` if needed.

## Skills that touch PersonalOS

When creating a skill for a PersonalOS vertical (e.g. LinkedIn, freelance, GTM):

1. **SKILL.md** lives in `.claude/skills/{name}/` (agent discovery)
2. **User-facing refined docs** live in `PersonalOS/{area}/`
3. **Scripts + data** live under `.claude/skills/{name}/scripts/` and `data/`
4. Skill workflow: interview or intake → user raw input → light refine → save `.md` draft to PersonalOS

## Folder hygiene

- No empty scaffold folders
- No `research/raw/`, `misc/`, `tmp/` inside PersonalOS
- Drafts are markdown; delete or archive old drafts to `90_Archive/` when stale

## Cross-reference

Agent reads PersonalOS for context. PersonalOS never depends on agent tooling paths for the user to browse manually.
