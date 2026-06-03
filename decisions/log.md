# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-06-02 — Created GTM Brainstorming Resource Folder

**Decision:** Created the `PersonalOS/40_Resources/GTM Brainstorming/` folder containing a README index, a Jordan Crawford & Blueprint GTM framework guide, and a reusable Brainstorming Workbook template.

**Why:** Rahi requested a dedicated folder path for fluff-free GTM brainstorming based on real practitioners. Storing this under `40_Resources` keeps the Obsidian vault organized according to the EXPANSIONS guidelines (flat structure under resources, reusable templates in a dedicated workbook, rather than raw document dumps).

**Alternatives considered:** 
- Placing it directly in the root of `PersonalOS` (rejected: clutters root directories).
- Storing it in `50_Library/Frameworks/` (rejected: `40_Resources` fits active operational GTM assets better, and templates/workbooks belong as resources).

**Owner:** AIOS / Rahi Uppal

---

## 2026-06-02 — Created Experience Companies Analysis Resource

**Decision:** Created the `PersonalOS/40_Resources/Experience Companies Analysis.md` document analyzing 5 core pages of the 7 companies/entities in Rahi's career trajectory.

**Why:** Rahi requested a page-by-page research profile of all companies in his experience to understand what they do using a structured framework. Storing this under `40_Resources` keeps historical and client details consolidated, easily referenceable for building customized value propositions or GTM models.

**Alternatives considered:** 
- Creating separate files for each company in a sub-folder (rejected: too many small files; a single consolidated file is easier to search and parse in Obsidian).
- Appending the profiles directly to `Career & Education.md` (rejected: kept `Career & Education.md` focused on resumes/milestones, while company offerings live as a reference asset under `40_Resources`).

**Owner:** AIOS / Rahi Uppal

---

## 2026-06-02 — Compiled Blueprint GTM Playbooks Library

**Decision:** Created the `PersonalOS/40_Resources/GTM Brainstorming/Playbooks/` directory containing a README index and 20 industry-specific markdown files compiling all 503 GTM Playbooks.

**Why:** Rahi requested a scraping of all 503 playbooks from the Blueprint GTM showcase to serve as copywriting and messaging skills. Storing these grouped by industry under `40_Resources/GTM Brainstorming/Playbooks/` keeps the vault highly organized, easy to query, and structured as a direct reference asset for B2B email/messaging creation.

**Alternatives considered:**
- Creating a single huge file (rejected: 503 detailed playbooks in a single markdown file would cause Obsidian performance lag and make browsing/linking difficult).
- Storing them directly under `references/` (rejected: references should remain focused on general frameworks/voice/SOPs; large-scale scraped data is better situated as operational resources under `40_Resources`).

**Owner:** AIOS / Rahi Uppal

---

## 2026-06-02 — Created Amply Retail Outreach Plays

**Decision:** Created the `PersonalOS/40_Resources/GTM Brainstorming/Amply Retail Outreach Plays.md` document outlining three highly targeted cold outreach campaigns for Heads of Retail in the US.

**Why:** Rahi requested a customized messaging playbook for Amply targeting retail personas in the US. The plays are structured around the newly integrated GTM frameworks (PQS, PVP, EDP), using specific triggers like negative facility reviews, new store expansions, and manual tasks in job descriptions to deliver upfront value.

**Alternatives considered:**
- Adding it directly to `Amply GTM Automation.md` (rejected: that file is project/engineering-focused, while messaging campaigns fit better under the GTM Brainstorming resource folder).

**Owner:** AIOS / Rahi Uppal

---

## 2026-06-03 — Created NRF Data Service Campaign Assets

**Decision:** Segmented the main `Global enriched.csv` NRF attendee database into `nrf_campaign/nrf_retailers.csv` (2,428 leads) and `nrf_campaign/nrf_exhibitors_filtered.csv` (1,880 leads, after filtering out 311 enterprise tech giants). Created `nrf_exhibitor_outbound_strategy.md` in the brain artifacts directory, and built `nrf_campaign/nrf_overlap_audit.py` to automate lead matching for exhibitors.

**Why:** Rahi requested a B2B GTM campaign strategy to monetize the NRF retailer delegate data by selling it to small-to-medium B2B exhibitors who sell to retailers. Clean segmentation and a custom matching script are required to run automated, permissionless audits (PVPs) for interested exhibitors, isolated in a root-level `nrf_campaign` folder.

**Alternatives considered:**
- Sending the entire attendee list raw to exhibitors (rejected: low value, high friction, and risk of data exposure. Delivering segmented lists or overlap audits provides a much stronger PVP hook).
- Manually matching leads in Excel (rejected: highly repetitive, error-prone, and doesn't scale. A Python CLI matching script enables instant, accurate CSV overlap reports).

**Owner:** AIOS / Rahi Uppal

---

## 2026-06-03 — Updated Outbound Email Generation Prompts & Fallbacks

**Decision:** Updated the OpenAI prompt and fallback dictionaries inside `nrf_outbound_generator.py` to align Emails 2 and 3 with the GTM strategy playbook (Lead Overlap Match Audit and Done-For-You Outreach Automation plays).

**Why:** Rahi noted that Emails 2 and 3 were generating generic, salesy follow-up drafts instead of leveraging the specific, value-driven playbook plays (offering a free mismatch audit and a setup of an automated n8n/Smartlead outreach pipeline). Hardcoding these playbook templates in both the LLM instructions and fallback code blocks ensures high consistency.

**Alternatives considered:**
- Keeping generic templates and relying on post-processing (rejected: adding explicit templates to the prompt guarantees the AI writes matching copy first-time, and keeping fallback dictionaries updated ensures safety on scrape/API failure).

**Owner:** AIOS / Rahi Uppal

---

## 2026-06-03 — Added Cache/Resume Support for Outbound Generator

**Decision:** Implemented a pre-run cache-loading mechanism in `nrf_outbound_generator.py` that parses `nrf_exhibitors_with_emails.csv` and skips scraping and LLM calls for any company that has already been successfully personalized.

**Why:** The script takes a significant amount of time to run across all 313 companies (due to network timeout wait periods and API limits). Resuming from an interruption previously resulted in overwriting output progress and re-running expensive OpenAI API calls from the beginning. Caching allows the script to pick up right where it left off.

**Alternatives considered:**
- Writing to a temporary database or JSON state file (rejected: reading the output CSV directly is simpler, keeps the codebase lightweight, and maintains a single source of truth for execution state).

**Owner:** AIOS / Rahi Uppal

---

## 2026-06-03 — Created Local Batch Filter & Upload Utility

**Decision:** Created the `nrf_campaign/send_batch.py` script to filter, deduplicate, clean, and batch 10 random leads from the NRF dataset, and upload them to Smartlead.

**Why:** Rahi requested batching and sending 10 leads while excluding Amply itself, its direct competitors, and enterprise giants (e.g. Microsoft, Salesforce). Since the user preferred not to use the Smartlead MCP server due to privacy concerns, we built a local CLI tool that filters, deduplicates to exactly one senior decision-maker per company, cleans the company names, and uploads the leads using the local `SMARTLEAD_API_KEY` from their environment or terminal prompt.

**Alternatives considered:**
- Directing the user to upload via the CSV import in the Smartlead UI (rejected: more manual work; the local script automates the payload structure and custom fields mapping, making it a single command).
- Continuing to use the Smartlead MCP server (rejected: explicitly requested to avoid using the MCP server to preserve account privacy).

**Owner:** AIOS / Rahi Uppal

---

## 2026-06-03 — Updated Hook Timeline Phrasing to Past Continuous

**Decision:** Updated the outreach Email 1 hook from "I saw you exhibited at NRF this year" to "I saw you were exhibiting at NRF Singapore this year" in the OpenAI prompt, fallback dictionaries, and retroactively updated all 1,878 generated email bodies in `nrf_exhibitors_with_emails.csv`.

**Why:** Since NRF Singapore runs from June 2 to June 4, 2026, and today is June 3, using simple past tense ("exhibited") would feel premature during the show. Using past continuous ("were exhibiting") remains correct during the active event (referencing their ongoing presence) and scales seamlessly for post-event outreach, ensuring the copy is temporally accurate and human-written long-term.

**Alternatives considered:**
- Using "I saw you are exhibiting" (rejected: would sound outdated once the event finishes).
- Splitting campaigns into "during" and "post" versions (rejected: increases operational complexity; a single past continuous hook covers both windows naturally).

**Owner:** AIOS / Rahi Uppal

