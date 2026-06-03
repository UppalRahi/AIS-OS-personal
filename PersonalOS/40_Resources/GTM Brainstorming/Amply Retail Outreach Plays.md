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

---

## 🔵 Play 4: The "Event / Conference Booth" Sequence

### 1. The Situation
The target prospects (Heads of Retail Operations) are attending a retail trade show or conference where Amply has a physical booth. Because floor traffic is hectic, standard "book a meeting" calls fail, and they need a low-friction hook to engage during or right after the event.

### 2. The Trigger
Exhibitor list matching + LinkedIn status updates or location-based event filters identifying that the ICP prospect is attending the conference.

### 3. The Permissionless Value Proposition (PVP)
Interactive mobile checklist demo links (test the interface on their own phone without visiting the booth) or post-event operational blueprints (e.g. transitioning from WhatsApp checklists to automated tasks).

### 4. Sequence Messages

#### ✉️ Message 1: Initial Outreach (Campaign 1)
> Hi `{first_name}`, inviting you to our Amply booth # 2215 (lower level). We digitize store tasks, VM executions, area manager visits into one app for Levi's, Miniso, FootLocker - would love to understand how your store operations are run today at `{company_name}` ✅ Maybe even show you a 5-min demo on the spot. We haven’t been introduced properly, but I’m Anshika, Founder at Amply - easily reachable at +91-9677-346-737 if you can’t find us at the venue 😄 - more on us at getamply.co

#### ✉️ Message 2: Targeted Follow-up (Campaign 2)
> Hello `{first_name}`, would love to meet you at Amply Booth # 2215 (lower level) if you’re visiting today. We’ll show you a demo on how we digitise store checklists, area manager audits, maintenance tickets into one app for 170+ retail chains like Kanmo, Adidas, Belgian Waffle, ASICS ✅ And help you with automations if your store tasks/SOPs are still done manually in paper, excel, Whatsapp 😄 Our booth is at Innovators’ Showcase Entry Gate (lower level). Looking forward!

#### ✉️ Message 3: Drip Options (Campaign 3)

##### Option A: The "Busy Floor / PVP" Play (During Event - Day 2/3)
> Hi `{first_name}`, since the show floor is usually crazy busy, I put together a quick mobile-friendly preview of how we digitize store checklists for Adidas and Levi's ✅ No need to stop by our booth, you can test-drive the task interface directly on your phone: getamply.co/mobile-demo 📱 We're at Booth #2215 (lower level) if you want to see the back-end compliance dashboard before the event ends. Safe walking!

##### Option B: The "Last Day / Urgent Sweep" Play (Final Day of Event)
> Hello `{first_name}`, final day of the event! We’re wrapping up at Amply Booth #2215 (Innovators’ Showcase, lower level) around 3 PM today. If you have 3 mins before you head out, swing by to see how Miniso runs VM photo audits on the spot. Otherwise, would it be helpful if I dropped a 1-page PDF here showing the checklist templates we use for retail chains? Safe travels! 😄

##### Option C: The "Post-Event WhatsApp Friction" Play (1-2 Days Post-Event)
> Hi `{first_name}`, hope you've recovered from the conference! I know how hectic the show floor gets, so no worries if you couldn't make it to Booth #2215. A big topic we discussed with other retail ops leads was the 'WhatsApp lag' — how district managers waste 4+ hours a week chasing store managers for photo check-ins. I put together a quick case study showing how Kanmo moved 170+ stores from WhatsApp to automated checklists ✅ more at: getamply.co/case-study - are your store SOPs still manual or on WhatsApp/Excel at `{company_name}`?

---

## 🎨 Campaign 2: Re-engagement Outbound Sequences (Playbook Style - Plain Text)

These sequences follow the GTM Playbook framework: direct, data-focused, starting straight with the operational problem, and ending with a low-friction question. They contain no links or attachments, and only use the standard variables: `{{first_name}}` and `{{company_name}}`.

### ✉️ Option 1: The "Excel & WhatsApp Lag" Play (PQS)
*   **Target Pain**: The operational time lost coordinating checklists and audits over unstructured messaging platforms.
*   **Variables**: `{{first_name}}`, `{{company_name}}`

> **Subject**: daily checklists at `{{company_name}}`
> 
> `{{first_name}}` - most retail teams scaling past 10 locations lose 4+ hours a week per manager just chasing daily checklists and area audits over WhatsApp and Excel.
> 
> When SOP compliance drops at a location, regional leaders usually only find out weeks later during manual reviews.
> 
> We help brands like Footlocker and Miniso digitize daily tasks and audits into a single mobile feed, giving district leaders real-time compliance dashboards.
> 
> Are store tasks at `{{company_name}}` still managed on Excel or WhatsApp, or have you digitized this process?

---

### ✉️ Option 2: The "Leadership Visibility Gap" Play (PQS)
*   **Target Pain**: Lack of real-time visibility into visual merchandising (VM) setups and store compliance.
*   **Variables**: `{{first_name}}`, `{{company_name}}`

> **Subject**: store SOP compliance at `{{company_name}}`
> 
> `{{first_name}}` - verifying that visual merchandising setups and opening checklists are done correctly across stores usually requires regional travel or chasing managers for photos on WhatsApp.
> 
> This lag makes it difficult to see store-wise completion rates on daily store tasks in real-time.
> 
> We help retail operations teams move daily checklists, VM photo audits, and area visits into one mobile app.
> 
> Are you still managing store operations manually at `{{company_name}}`?

---

### ✉️ Option 3: The "Floor-Time Recovery" Play (PQS)
*   **Target Pain**: Quantified floor-time lost to manual paper logs and compile times.
*   **Variables**: `{{first_name}}`, `{{company_name}}`

> **Subject**: retail operations at `{{company_name}}`
> 
> `{{first_name}}` - having store managers compile daily logs and maintenance tickets manually costs an average of 4.5 hours of floor-time per store, per week.
> 
> When field teams manage operations on paper or unstructured email chains, compliance tracking is almost impossible.
> 
> We digitize daily store checklists, communications, and area audits into one mobile feed for retail chains.
> 
> Do you think a mobile-first checklist tool could help streamline tasks at `{{company_name}}`?




