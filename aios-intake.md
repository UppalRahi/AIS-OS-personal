# AIS-OS Intake

This is the source-of-truth file for your AIOS. Fill it in by typing, voice-pasting (Wispr Flow / OS dictation), or running `/onboard` for a guided conversation. Whichever mode, this file is what `/onboard` reads to scaffold your Day-1 setup.

**Hard cap: 7 questions.** Each answerable in under 60 seconds. Don't overthink — you can edit and re-run `/onboard` any time.

---

## Q1 — Who are you, what do you sell, who do you sell it to?

Identity, offer, ICP. One paragraph each is fine.

```
Identity: Rahi Uppal, a Mechanical Engineering graduate from NIT Srinagar (CGPA 8.12/10) who fell in love with robotics and automation. I transitioned into AI automation, GTM (Go-To-Market) systems engineering, and workflow architecture. I have co-founded two startups (Traway and BoldBites/The Loud Kitchens) and completed high-leverage internships/roles at IIT Delhi, Ecoyaan, Varidus (Singapore), GrowthJockey, and Amply (Google-backed).

Offer: n8n Workflow Architecture and GTM Automation engineering. I design and build event-driven, production-grade workflow systems, multi-channel AI orchestration pipelines (email, LinkedIn, WhatsApp), and data layers (SQLite, Looker Studio) that scale B2B outreach, automate lead enrichment, and optimize operational efficiency.

ICP (Ideal Customer Profile): B2B startups, venture builders, family offices, and high-growth brands (like Amply, Varidus, and GrowthJockey) looking to automate their GTM motions, build custom AI-assisted workflow engines, and slash operational overhead.
```

---

## Q2 — Paste 1-2 things you've written recently. Don't edit them.

An email, a LinkedIn post, a DM, a doc — anything that sounds like you when you're not trying. **Paste verbatim.** Do not type these mid-conversation with Claude — chat-shaped samples are worse than no samples (voice contamination).

```
Sample 1 (From SOP - Background & Resilience):
Growing up in a small village near the Line of Control in Jammu and Kashmir, I was acutely aware of how external instability could disrupt livelihoods. This reality shaped my determination to create opportunities for my community. Years later, during my entrepreneurial journey, I found that data could reveal hidden trends and power decisions that deliver real impact. While managing The Loud Kitchens at NIT Srinagar, I analysed customer data and uncovered actionable insights that increased engagement and revenue by 11%. This moment solidified my belief in analytics as a means to drive meaningful change.
```

```
Sample 2 (From SOP - Engineering & Startups):
My academic background in Mechanical Engineering at NIT Srinagar enhanced my quantitative and problem-solving skills. Beyond coursework, my entrepreneurial ventures, such as Traway Travels, allowed me to apply analytics to optimise operations and increase revenue by 15% within eight months. These experiences underscored the power of data-driven decision-making. Independent projects deepened my technical expertise. Using Python and Tableau, I analysed Amazon India sales data to uncover trends and build actionable dashboards.
```

---

## Q3 — What are your 2-3 biggest priorities for the next 90 days?

Quarterly priorities. Not yearly aspirations. Things that, if not done by July, would make you say "I wasted Q2."

```
1. Build out and scale my Personal OS in Obsidian as an evergrowing second brain for my personal and professional life.
2. Optimize and expand GTM AI orchestration pipelines at Amply (saving more time and driving more B2B meetings).
3. Level up my technical stack around API integrations, custom MCP servers, and LLM-assisted workflows.
```

---

## Q4 — Where does revenue actually land, and where is it tracked?

Multiple answers OK. Stripe? Skool? GoHighLevel? QuickBooks? A spreadsheet?

```
Amply business revenue tracked via HubSpot and internal databases. Personal finances and previous startup metrics tracked via Google Sheets and bank accounts.
```

---

## Q5 — Where do you talk to customers, your team, and the outside world day-to-day?

Email (which one — Gmail / Outlook)? Slack? Teams? DMs (Skool / Discord / iMessage)? Phone?

```
- Internal team & clients: Slack, Gmail (er.rahiuppal@gmail.com)
- Outbound outreach: Smartlead, LinkedIn, WhatsApp (WABA)
- Community & networking: LinkedIn DMs, WhatsApp
```

---

## Q6 — Where do meeting recordings, notes, and important docs live?

Granola? Otter? Fireflies? Google Drive? Notion? Dropbox? A folder on your desktop you keep meaning to organize?

```
- Active docs & notes: Obsidian (PersonalOS vault)
- Company assets & databases: Google Drive, Looker Studio, SQLite database
```

---

## Q7 — What's the one task that eats your week, and where do you currently track work?

The single biggest time-suck or recurring drudgery. Plus where tasks/projects live (ClickUp / Asana / Linear / Notion / a notebook).

```
- Task tracking: Obsidian (PersonalOS vault)
- Biggest weekly time-sucks: Lead list curation, enrichment and verification pipelines, and debugging multi-channel outreach campaigns.
```

---

When this file is filled, run `/onboard` (or re-run it) and the wizard will scaffold your Day-1 file set: `context/`, `references/voice.md`, populated `connections.md`, and a filled `CLAUDE.md`.
