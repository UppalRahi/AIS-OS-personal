# Amply: Retail Outreach Playbook

This document details three high-precision, trigger-based outreach plays for **Amply** targeting **Heads of Retail / VP of Retail Operations** in the United States. These plays avoid generic feature-pitching and instead leverage observable "existential data points" to deliver immediate value.

---

## 🟥 Play 1: The "Facility Friction" Review Trigger (PVP)

### 1. The Situation
Store managers are failing to maintain basic operational standards (restroom cleanliness, lighting, display issues), causing customers to leave negative public reviews. Regional managers only find out weeks later during manual audits.

### 2. The Trigger (Existential Data Point)
Scrape Google Maps/Yelp reviews for the prospect's retail locations. Filter for reviews in the last 30 days containing keywords like: `dirty`, `broken`, `messy`, `lights out`, `restroom`, `trash`.

### 3. The Permissionless Value Proposition (PVP)
A custom **"Store Cleanliness & Maintenance Audit"** showing a summary of negative operational reviews mapped by location, showing the Head of Retail where local checklist compliance is slipping.

### 4. Outreach Message Draft
> **Subject**: `{{Location Count}}` facilities feedback for `{{Company Name}}`
> 
> Hi `{{First Name}}`,
> 
> I ran a quick filter across reviews for your `{{State}}` stores last month. 
> 
> `{{Review Count}}` customer reviews mentioned facility issues—mostly `{{Primary Issue, e.g. dirty restrooms / broken displays}}` at your `{{City}}` location.
> 
> When these slip, it usually means local store managers are managing opening checklists manually or via WhatsApp.
> 
> I put together a quick 3-column sheet showing the exact review locations and timestamps:
> 
> `[Link to Google Sheet]`
> 
> We built a tool called Amply that digitizes these checklists with photo-verification so you see store standards in real-time. 
> 
> Let me know if you want the checklist templates we use for retail groups.
> 
> Best,
> Rahi

### 5. Automated Data Pipeline
- **Enrichment**: Clay (search for all Google Maps listings under `{{Company Name}}` brand).
- **Filtering**: Script to extract and analyze reviews from the past 30 days using NLP/keywords.
- **Orchestration**: n8n workflow aggregating results into a Google Sheet and enrolling the contact in a Smartlead campaign.

---

## 🟨 Play 2: The "Visual Merchandising" Expansion Trigger (PVP)

### 1. The Situation
The retail brand is opening new locations or launching a new product campaign. Coordinating visual merchandising (VM) rollouts and display setups across 20+ locations is hard to verify without regional travel.

### 2. The Trigger (Existential Data Point)
The retail brand announces `{{X}}` new stores "Coming Soon" or listed on their site, *OR* public job postings show they are hiring a "Visual Merchandiser" in a specific state.

### 3. The Permissionless Value Proposition (PVP)
A custom **"Visual Merchandising Compliance Map"** showing a quick flowchart of how district managers can verify display compliance in under 5 minutes using automated photo verification.

### 4. Outreach Message Draft
> **Subject**: VM compliance at your new `{{City}}` store?
> 
> Hi `{{First Name}}`,
> 
> Congrats on the new store opening at `{{Street Address}}` in `{{City}}`.
> 
> As you scale locations, verifying that new visual merchandising displays are set up correctly usually requires regional managers to travel or manually chase store managers over text.
> 
> I mapped out a simple photo-verification workflow showing how district managers can audit VM compliance across all `{{Total Stores}}` locations from their desk:
> 
> `[Link to Mermaid/Workflow Diagram]`
> 
> It lets store managers submit time-stamped photos of their main displays, automatically flagging anomalies.
> 
> Let me know if you want the mobile VM checklist template we built for this.
> 
> Best,
> Rahi

### 5. Automated Data Pipeline
- **Enrichment**: Google Search API or career pages monitoring for "new store", "coming soon", or "grand opening" announcements.
- **Orchestration**: n8n workflow monitoring RSS news feeds for the brand.

---

## 🟩 Play 3: The "Manual SOP Coordinator" Job Post Trigger (PQS)

### 1. The Situation
The company is hiring retail managers and their job descriptions reveal they are still relying on manual reporting, paper logs, or unstructured coordination tools (like Excel or WhatsApp).

### 2. The Trigger (Existential Data Point)
Active job postings on LinkedIn/Indeed for "Store Manager", "District Manager", or "Operations Lead" containing phrases like: `compile daily reports`, `WhatsApp checklist`, `Excel tracking`, or `manual inventory audit`.

### 3. The Permissionless Value Proposition (PVP)
A comparison table showing the time-savings of digitized checklists vs. manual Excel compile times (saving an average of 4.5 hours per store manager per week).

### 4. Outreach Message Draft
> **Subject**: Operations bottleneck in your `{{Job Title}}` listing
> 
> Hi `{{First Name}}`,
> 
> I saw you're hiring a `{{Job Title}}` in `{{City}}`.
> 
> The description mentions they will be responsible for `{{Manual task, e.g. manually compiling daily opening checklists and maintenance logs}}`.
> 
> Typically, having managers compile these manually costs about 4-5 hours of floor-time per week, per store.
> 
> We built a digitized operations template for retail teams that automates opening audits and maintenance ticketing directly from a mobile feed:
> 
> `[Link to Amply Mobile Demo Checklist]`
> 
> It eliminates manual compile time and syncs compliance data to your dashboard instantly.
> 
> Open to seeing how it works?
> 
> Best,
> Rahi

### 5. Automated Data Pipeline
- **Enrichment**: Clay / Apify (scraping LinkedIn Jobs for the target ICP brands).
- **Filtering**: Regex checking job descriptions for operational keywords (e.g. `Excel`, `manually`, `compile`).
- **Outreach**: n8n routes the contact details to HubSpot and enlists them in Smartlead.
