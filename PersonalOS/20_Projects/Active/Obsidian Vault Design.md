# Project: Obsidian Vault Design

## Objective
Design a premium, visual, and highly functional Personal OS within Obsidian. The vault should steer personal life, active projects, tasks, and reference libraries.

---

## Vault Structure Overview

- `00_System/` - Symlinked AIOS configurations and inputs.
- `10_Life_OS/` - Vision, career trajectory, financial trackers.
- `20_Projects/` - Active workstreams and backlog.
- `30_Daily_Log/` - Structured daily logs, templated weekly reviews.
- `40_Resources/` - n8n playbooks and industry research.
- `90_Archive/` - Stale notes and logs.

---

## Recommended Core Community Plugins

To transform this vault into a dynamic, interactive dashboard, we recommend installing the following community plugins:

### 1. **Dataview**
- *Why*: Allows you to query your vault using SQL-like syntax.
- *Use Case*: List all active projects automatically on your home note or compile tasks from daily notes.

### 2. **Templater**
- *Why*: Advanced templates using JavaScript.
- *Use Case*: Insert dynamic dates, priorities, and automated structures when creating new daily logs.

### 3. **Minimal Theme + Minimal Theme Settings**
- *Why*: Provides a clean, modern, card-based aesthetic.
- *Use Case*: Styling Dataview tables into clean cards for dashboards.

### 4. **Calendar**
- *Why*: Visual calendar view in the sidebar.
- *Use Case*: Clicking a calendar date automatically creates or opens that day's daily log note.

---

## Configuration Action Items

- [x] Create structured, numbered folder layout.
- [x] Link repository-level AIOS files to `00_System/`.
- [ ] Create dashboard home note (`Home.md`).
- [ ] Install and configure community plugins (Dataview, Templater).
- [ ] Set up hotkey shortcuts (e.g., `Cmd + D` to open today's daily log).
