# Connections

Registry of every system your AIOS can reach. Expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | HubSpot / Google Sheets | not yet connected | — | — |
| 2 | Customer interactions | HubSpot CRM / LinkedIn / WABA | not yet connected | — | — |
| 3 | Calendar | Google Calendar | not yet connected | — | — |
| 4 | Communication | Gmail / Slack / Smartlead | not yet connected | — | — |
| 5 | Project / task tracking | Obsidian (`PersonalOS` vault) | not yet connected | — | — |
| 6 | Meeting intelligence | None | not yet connected | — | — |
| 7 | Knowledge / files | Obsidian / Google Drive / SQLite | not yet connected | — | — |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.
