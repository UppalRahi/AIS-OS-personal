# Jordan Crawford & Blueprint GTM

- **LinkedIn**: [Jordan Crawford](https://www.linkedin.com/in/jordancrawford/)
- **Website**: [Blueprint GTM](https://blueprintgtm.com/)
- **Core Concept**: **GTM Engineering** — treating outbound and Go-to-Market strategy as a technical system to be engineered, rather than a manual sales exercise.

---

## 🧠 Core Frameworks & Methodologies

### 1. Go-to-Market (GTM) Engineering
Instead of standard RevOps (which is historical and report-focused), **GTM Engineering** is proactive and technical. 
- **Method**: Start by defining the *exact, perfect message* that would convince your highest-value prospect to buy. Then, reverse-engineer the data sources, scrapers, APIs, and AI logic required to build and verify that message at scale.

### 2. Situational Targeting (PQS - Pain-Qualified Segments)
Traditional outbound targets "personas" (e.g., VP of Sales, CTO). Crawford argues personas are lazy. Buyers don't buy because of their job title; they buy because of a **situation** they are currently in.
- **PQS**: A group of companies undergoing a specific, observable operational tension point (e.g., a company scaling their sales team while their HubSpot data is messy, or a company experiencing high email bounce rates).

### 3. The Existential Data Point (EDP)
The ultimate filter for list-building. It is the single data signal that differentiates a company that *urgently needs* your solution from a company that does not.
- *Example*: If you sell email deliverability consulting, the EDP is not "companies who send email"; it is "companies whose MX records are misconfigured or who have been blacklisted on Spamhaus."

### 4. Permissionless Value Proposition (PVP)
Instead of asking a prospect for 15 minutes of their time to pitch them (which creates friction), you deliver **value upfront** without permission.
- **Mechanism**: Use AI/scraping to analyze their business, find an issue, suggest the fix, and present it clearly. Make the outreach email so insightful that the recipient would have been willing to pay for it as a stand-alone report.

### 5. The FIND Process
A structured roadmap for executing GTM Engineering campaigns:
- **Focus**: Identify the Pain-Qualified Segment (PQS) and its Existential Data Point (EDP).
- **Investigate**: Scrape, query, and gather the custom data signals using tools like Clay, custom APIs, and AI models.
- **Narrate**: Programmatically translate the raw data signals into natural, highly personalized copy (using LLMs for variable injection and message structuring).
- **Deploy**: Send the campaign through high-deliverability cold email channels (e.g., Smartlead) or automated LinkedIn sequences.

### 6. Cannonball GTM
Unlike a "cannon" (a huge, slow, generic email blast), a **Cannonball GTM** campaign is:
- **High-Precision**: Small batch sizes (50–500 target accounts).
- **Hyper-Targeted**: The pain point is verified through custom code before sending.
- **Iterative**: Fast execution cycles to test if a specific trigger translates to high reply rates.

---

## 🛠️ Actionable Triggers & Heuristics (No Fluff)

Jordan Crawford advocates for building **bespoke data moats** rather than buying standard Apollo lists. Here are examples of high-intent, situation-based triggers:

| Trigger Category | Specific Signal | Pain Indicated | Actionable PVP Angle |
| :--- | :--- | :--- | :--- |
| **Job Postings** | Hiring a role that mentions specific legacy tools or manual processes (e.g., "Must be proficient in manual data entry using Excel and Salesforce"). | Inefficient operations, manual workflows, ready for automation. | "I saw you are hiring a Sales Coordinator to handle X and Y manually. We built an n8n workflow that handles that automatically—here is how it works..." |
| **Tech Stack Shifts** | Removing a competitor's tracking script or installing a new complex tool (e.g., installing HubSpot but lacking connected DNS). | Transition phase, operational gaps, implementation pain. | "I noticed you just installed HubSpot but your domain setup is missing X record, which could land your team's invites in spam. Here is the configuration to fix it." |
| **Product Deficiencies** | slow web app load times, broken links in help centers, or broken API endpoints. | Quality assurance bottlenecks, engineering team is stretched thin. | "I was checking your site and noticed your main API endpoint is returning a 504 on this query. Here is the exact request payload that failed so your dev team can patch it." |
| **Outbound Signals** | Identifying that their reps are sending emails with poor deliverability setups (detected via SPF/DKIM checkers). | Low pipeline yield, domains at risk of suspension. | "We received a cold mail from your rep and noticed X domain lacks DKIM validation. Here is the DNS line to paste in Cloudflare to keep your outreach out of spam." |
