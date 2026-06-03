# Strategic GTM Outbound Playbook: Monetizing NRF Retailer Data

This strategic document outlines how to position, segment, and sell the verified NRF **Delegate (Retailer)** dataset to NRF **Exhibitor** companies (excluding big tech giants). It is built on GTM Engineering and Situational Outbound principles.

All campaign files and matching scripts reside in the dedicated folder in the current directory: [nrf_campaign/](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/).

---

## 📊 NRF Lead Database Overview

Based on the [Global enriched.csv](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/Global%20enriched.csv) database analysis:
- **Total Attendee Leads**: 5,723
- **Exhibitors**: 1,880 clean leads (excluding enterprise tech giants) saved in [nrf_exhibitors_filtered.csv](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_exhibitors_filtered.csv).
- **Delegates (Retailers)**: 2,428 leads across 1,454 unique retail brands saved in [nrf_retailers.csv](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_retailers.csv).
- **Retail Decision-Maker Titles**: 85 Directors, 66 Managers, 53 General Managers, 39 CEOs, 27 IT Managers, 24 Marketing Directors.

---

## 🎯 The Pain-Qualified Segment (PQS)

Exhibiting at NRF is a massive capital and time investment. 

### 1. The Situation
SMB/Mid-Market exhibitors spend **$15k to $100k+** to set up a booth, fly out sales teams, and print collateral. However, after the show, they suffer from **Event Lead Leakage**:
* **Low Lead Density**: Most high-value retail decision-makers walked past their booth without stopping.
* **Low-Quality Badges Scanned**: Reps scanned low-level managers or job-seekers grabbing swag, missing the actual budget holders.
* **High Post-Show Friction**: Sales reps are back to cold calling generic lists because their post-event spreadsheet only has 50–80 leads.

### 2. The Trigger (Existential Data Point)
* **EDP**: The B2B company is listed as an NRF Exhibitor (excluding fortune 500 tech like Microsoft, Salesforce, SAP, Oracle) **AND** has an active sales presence on LinkedIn.
* **Their Need**: They sell *directly to retailers* and urgently need high-intent retail leads to justify their heavy NRF investment.

### 3. The Permissionless Value Proposition (PVP)
Instead of asking for a call, you deliver upfront value:
1. **The Target Niche Sample**: Send them 3–5 verified retail leads that fit their *exact target buyer profile* who attended NRF but did not scan their booth.
2. **The "Lead Overlap" Audit**: Offer to cross-reference their scanned lead list against your master database of 2,428 retail delegates to show them exactly which accounts they missed using the local matching tool: [nrf_overlap_audit.py](file:///Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_overlap_audit.py).

---

## 🗺️ Exhibitor Target Matrix (Slicing the Data)

You must segment the 2,428 Retailer Delegates based on what the target Exhibitor sells.

| Exhibitor Type | Target Exhibitor Examples | Retailer Target Persona | Example Target Retailers from CSV |
| :--- | :--- | :--- | :--- |
| **POS / Retail Hardware** | *Woosim Systems, Urovo, Shenzhen Sunany* | IT Managers, Store Ops Directors, CIOs | *Marina Bay Sands (Group IT Business Partner), AEON Smart Tech (IT Lead)* |
| **Supply Chain / Inventory Software** | *GenieX (Relex Solutions), MileApp* | Procurement Directors, Supply Chain Managers | *Jaya Grocer (Director - Grocery Procurement), Little Farms (Head of Store Ops)* |
| **Retail Media / Marketing Tech** | *Osmos, TransPerfect, Lark* | E-commerce Merchandisers, Marketing Directors | *& Other Stories (E-commerce Merchandiser), Castlery (Marketing Director)* |

---

## ✉️ The 3-Step Outbound Email Sequence

These emails use a low-friction, founder-led tone and offer immediate, tangible data to get replies.

### Email 1: The NRF Follow-up Leak
* **Goal**: Highlight their NRF investment and offer a personalized sample of missed leads.

```text
Subject: NRF follow-up gap for {{Company Name}}

Hi {{First Name}},

I saw you exhibited at NRF this year. 

While your team likely scanned badges at the booth, NRF had 2,428 unique retail delegates (representing 1,454 brands like FairPrice, Castlery, and Sephora) walking the floor. Most exhibitors only capture 5-10% of their target market due to booth bypass or reps scanning lower-level staff.

I compiled and verified the list of these 2,428 retail delegates, including direct emails, phone numbers, and official titles.

I ran a quick filter for {{Company Name}}'s target buyer profile and found {{Count, e.g., 42 retail IT and store operations directors}} who attended the show.

I'd be happy to send over a sample sheet with 5 of these contacts so your team can verify their NRF attendance status. 

Want me to drop the sample list here?

Best,
Rahi
```

---

### Email 2: The "Missed Accounts" Comparison
* **Goal**: Provide social proof and offer a free custom lead-matching audit.
* **Timing**: Sent 3 days after Email 1.

```text
Subject: The {{Target Retailer Category}} NRF list

Hi {{First Name}},

Following up on my last note. To give you an idea of the retail footprint at the show:

Retailers like FairPrice Group sent 78 delegates, Castlery sent 33, and Sephora sent 10. 

If your sales team is currently doing generic cold outreach, they are likely missing the fact that these exact retail ops and IT decision-makers were active at NRF looking for new solutions.

I set up a segmented sheet of the {{Target Retailer Category, e.g., grocery and apparel operations leads}} who were at the venue.

If you send me a list of the companies your team scanned at the booth, I can run a free overlap report to show you exactly which high-value retail targets walked by without scanning.

Open to running the match?

Best,
Rahi
```

---

### Email 3: The "Done-for-You" Outreach Close
* **Goal**: Transition from selling raw lists to selling a fully automated GTM campaign service (the "outreach machine").
* **Timing**: Sent 4 days after Email 2.

```text
Subject: outbound pipeline for {{Company Name}}'s NRF data

Hi {{First Name}},

Since I haven't heard back, I'm assuming you're either fully booked with NRF follow-ups or your reps are already working their scanned leads.

Beyond just buying the raw data of these 2,428 retail delegates, we build automated, multi-channel outbound systems (using n8n and Smartlead) to reach them directly.

Instead of your team manually emailing them, I can set up an automated sequence that emails the exact NRF retailer delegates you missed, referencing their attendance to book post-show demos.

I put together a quick diagram of how this outbound machine is structured:

[Link to Outbound Workflow Diagram]

Let me know if you want a copy of the workflow template.

Best,
Rahi
```

---

---

## 🧠 Play 5: The "Scraped Site Intelligence" Hyper-Personalization Play (PQS + PVP)

This play uses automated web scraping to dynamically deduce the exhibitor's target retail persona, then presents them with a custom list size matching their exact product.

### 1. The Enrichment Pipeline
Before sending any emails, the lead list of 1,880 exhibitors is passed through a scraper (e.g., Clay or an n8n HTTP scraper) to grab the homepage text. An LLM parses the scraped copy to output structured variables.

### 2. The LLM Prompt (For n8n / Clay AI Nodes)
```text
System Prompt:
You are an expert GTM engineer. Your task is to analyze scraped website copy from a B2B company's homepage and extract two specific data points to construct a hyper-personalized outbound campaign.

Output JSON format:
{
  "product_summary": "A 5-7 word summary of their product in the format 'help retail brands with [action]', e.g. 'help retail brands with last-mile delivery tracking' or 'help retail brands with POS checkout terminals'",
  "ideal_buyer_titles": "The main job titles/departments they target in retail, e.g. 'supply chain and logistics', 'e-commerce and merchandising', or 'IT and store operations'",
  "ideal_buyer_keywords": "A comma-separated list of keywords to search in a delegate database to find their buyers, e.g., 'supply chain, logistics, delivery, procurement'"
}
```

### 3. Personalization Mapping Examples
Using the scraped results, your database runs a query (`SELECT COUNT(*) WHERE title LIKE ideal_buyer_keywords`) to inject real numbers:
* **Exhibitor**: *MileApp* (scraped: `mile.app`)
  * `{{product_summary}}`: help retail brands with route optimization and delivery tracking
  * `{{ideal_buyer_titles}}`: supply chain and logistics
  * `{{Niche Retailers Count}}`: 54
  * `{{Examples Niche Retailers}}`: Jaya Grocer and Little Farms
* **Exhibitor**: *Osmos* (scraped: `osmos.ai`)
  * `{{product_summary}}`: help retail brands with retail media monetization
  * `{{ideal_buyer_titles}}`: e-commerce and digital marketing
  * `{{Niche Retailers Count}}`: 89
  * `{{Examples Niche Retailers}}`: & Other Stories and Castlery

---

## ✉️ Scraped Personalization Email Sequence

### Email 1: The Site-Scraped NRF Hook
* **Goal**: Show that you understand exactly what they sell and offer a custom, highly relevant slice of the NRF list.

```text
Subject: NRF follow-up gap for {{Company Name}}

Hi {{First Name}},

I saw you exhibited at NRF this year. 

Since {{Company Name}} {{product_summary}}, I assume your sales team was walking the floor looking to connect with {{ideal_buyer_titles}} decision-makers.

While you likely scanned a few badges, NRF had 2,428 unique retail delegates walking the floor—most of whom bypass booths.

I ran a quick query on our verified database of these delegates and mapped {{Niche Retailers Count}} active {{ideal_buyer_titles}} leads who attended the show, including decision-makers from brands like {{Examples Niche Retailers}}.

I put together a quick 3-column sheet with 5 verified contacts matching your target profile so your team can test the data quality. 

Want me to drop the sample list here?

Best,
Rahi
```

---

### Email 2: The Competitive Match Play
* **Goal**: Highlight the risk of using generic lists and offer a free lead mismatch check.
* **Timing**: Sent 3 days after Email 1.

```text
Subject: missing {{ideal_buyer_titles}} leads from NRF

Hi {{First Name}},

Following up on my last note. 

When B2B teams follow up after NRF, they often run standard outbound targeting generic lists. But the fact that retail decision-makers from brands like FairPrice, Castlery, and Sephora *physically attended* NRF makes them highly warm accounts.

I set up a targeted slice of the NRF database containing only the {{Niche Retailers Count}} {{ideal_buyer_titles}} delegates. 

If you want to send over a list of the companies your reps scanned at the show, I can run a quick check against our database to show you exactly which matching retail targets walked past your booth without scanning.

Would that be helpful for your sales team?

Best,
Rahi
```

---

### Email 3: The Outbound Campaign Offer
* **Goal**: Shift the offer from raw data to a fully managed GTM outreach pipeline (the "outreach machine").
* **Timing**: Sent 4 days after Email 2.

```text
Subject: outbound pipeline for {{Company Name}}'s NRF data

Hi {{First Name}},

Since I haven't heard back, I'm assuming your sales reps are fully occupied following up on the badges they scanned.

Beyond just selling raw datasets, we build automated, multi-channel GTM pipelines (using n8n and Smartlead) to reach NRF delegates.

Instead of your team manually writing emails, I can set up an automated sequence that reaches the exact {{Niche Retailers Count}} {{ideal_buyer_titles}} prospects you missed, mentioning their NRF attendance to schedule post-event demos.

I put together a quick diagram of how this outbound machine is structured:

[Link to Outbound Workflow Diagram]

Let me know if you want a copy of the workflow template.

Best,
Rahi
```

---

## 🛠️ The Pipeline Infrastructure (The Machine)

To deliver this service at scale, you can leverage your B2B automation stack:
1. **Exhibitor Domain Scrape (n8n / Clay)**:
   - Scrape homepage copy using Clay's HTTP scraping or n8n HTTP Request node.
2. **LLM Parsing (OpenAI API / Clay AI)**:
   - Run the structured LLM prompt over the text to generate `product_summary` and `ideal_buyer_keywords`.
3. **Database Segmenting (SQLite)**:
   - Query your `nrf_retailers.csv` database using the generated `ideal_buyer_keywords` to count the total matching leads and fetch 2 sample companies.
4. **Enrichment & Delivery (Smartlead API)**:
   - Enrich the target exhibitor contacts using Apollo/Clay (finding VP Sales/CEOs).
   - Inject the variables into your Smartlead sequence.

