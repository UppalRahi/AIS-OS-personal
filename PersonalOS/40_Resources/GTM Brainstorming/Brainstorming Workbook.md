# GTM Brainstorming Workbook

Use this workbook to brainstorm, scope, and plan hyper-targeted outbound campaigns. Copy the blank template section below for every new campaign you want to construct.

---

## 🚀 Campaign Sandbox (Template)

*Duplicate this section to start a new campaign brainstorm.*

### 1. The Offer
*What specific service or product are you offering, and what is the primary benefit?*
- **Offer**: 
- **Core Benefit**: 

### 2. Pain-Qualified Segment (PQS) & Situation
*What specific operational tension or transition is the company experiencing? (Move beyond job titles/personas)*
- **The Situation**: 
- **Why it's a priority now**: 

### 3. Existential Data Point (EDP) & Triggers
*What observable signal or combination of data points proves they are in this situation?*
- **EDP / Primary Signal**: 
- **Data Source(s)**: *(e.g., job postings, builtwith, DNS records, LinkedIn posts)*
- **Scraping / Verification Logic**: 

### 4. Permissionless Value Proposition (PVP)
*What upfront value can you deliver in the email to prove you understand their problem without asking for a meeting?*
- **Upfront Value**: *(e.g., a custom script, a DNS config fix, a screenshot of an issue, a free workflow diagram)*
- **PVP Delivery Format**: 

### 5. Outreach Script & Variables
*Draft the core email structure. Highlight the programmatically injected variables.*
- **Subject Line**: 
- **Body Draft**:
  > Hi `{{First Name}}`,
  > 
  > I noticed that `{{Company Name}}` is currently `{{Trigger/Situation description}}`.
  > 
  > I ran a quick check/script and found `{{Specific Insight/PVP details}}`.
  > 
  > Usually, this causes `{{Specific Pain point}}`. To fix this, you can:
  > 1. `{{Action step 1}}`
  > 2. `{{Action step 2}}`
  > 
  > I built a short `{{Resource/Workflow}}` that automates this. Let me know if you'd like me to send it over.
  > 
  > Best,
  > Rahi

### 6. Pipeline Infrastructure (The Machine)
*What tools and integrations are needed to automate this campaign?*
- **Data Enrichment**: *(e.g., Clay, Apollo, Custom Scrapers)*
- **Data Layer / State Control**: *(e.g., SQLite, Google Sheets)*
- **Orchestration**: *(e.g., n8n, Python)*
- **Outreach Channels**: *(e.g., Smartlead, LinkedIn API)*

---

## 💡 Pre-Populated Example: Lead Collision Prevention

*This is a real-world example of how Rahi can apply the GTM Engineering framework to sell n8n/SQLite data layer integrations to scaling startups.*

### 1. The Offer
- **Offer**: Custom SQLite + n8n centralized data layer setup.
- **Core Benefit**: Eliminates duplicate cold outreach (lead collision) across multiple Smartlead campaigns and sales reps, protecting domain reputation and customer experience.

### 2. Pain-Qualified Segment (PQS) & Situation
- **The Situation**: A high-growth B2B startup that is actively scaling its sales outreach team (hiring multiple SDRs/BDRs) and utilizing multiple outbound domains, but lacks a centralized data deduplication engine.
- **Why it's a priority now**: Multiple reps are emailing the same prospect simultaneously due to siloed lead lists. This destroys brand credibility and causes spam reports to spike.

### 3. Existential Data Point (EDP) & Triggers
- **EDP / Primary Signal**: 
  - Company is actively hiring for **2+ outbound roles** (SDR/BDR/Sales Rep) *AND*
  - Using **Smartlead** or **Instantly** (detected via email header checks on their outreach or job description keywords) *AND*
  - Has **no active RevOps lead** listed on LinkedIn (meaning the reps are likely managing their own lead lists in siloes).
- **Data Source**: LinkedIn Job Postings + Apollo (job titles) + Hunter.co / BuiltWith (email headers / tech stack).

### 4. Permissionless Value Proposition (PVP)
- **Upfront Value**: A customized database architecture diagram showing exactly how lead data flows from Apollo/Clay through a SQLite deduplication layer before hitting Smartlead, ensuring no lead is ever messaged twice.
- **PVP Delivery Format**: A 1-click mermaid flow diagram embedded in the email or a link to a private Miro template.

### 5. Outreach Script & Variables
- **Subject Line**: SDR collision at `{{Company Name}}`
- **Body Draft**:
  > Hi `{{First Name}}`,
  > 
  > I saw you're expanding your outbound team with new `{{Job Title}}` roles.
  > 
  > When scaling outbound across multiple reps, a major silent issue is **lead collision**—where the same lead gets emailed by two different reps or campaigns because Apollo/Clay lists overlap.
  > 
  > Since you're running `{{Outreach Tool}}`, I put together a simple database logic diagram showing how a lightweight SQLite engine can act as a single deduplication filter:
  > 
  > `[Mermaid Diagram Link]`
  > 
  > It automatically checks if a lead has been contacted in the last 90 days across *any* rep's inbox before sending.
  > 
  > Let me know if you want the n8n template for this logic—no strings attached.
  > 
  > Best,
  > Rahi

### 6. Pipeline Infrastructure (The Machine)
- **Data Enrichment**: Clay (to scrape job openings and find tech stack).
- **Data Layer / State Control**: SQLite database running on a VPS or local dev machine.
- **Orchestration**: n8n workflows (checking new leads against the SQLite master list).
- **Outreach Channels**: Smartlead API.
