# Resource: VC & Family Offices

This note outlines venture building strategies, capital matching systems, and startup analytics, drawing from advisory experience at **Varidus** (Singapore-based venture builder and consulting firm).

---

## 1. Varidus Context & Methodology

- **Focus**: Singapore-based consulting and venture builder connecting startups with Venture Capital (VC) firms, family offices, and corporate M&A.
- **The Challenge**: Family offices and VCs receive hundreds of pitch decks daily. Identifying high-potential startups and matching them with the right investment thesis requires intensive, high-leverage data sorting.
- **The Solution**: 
  - Conducted deep primary and secondary market research on family offices and Southeast Asia founders.
  - Developed an interactive BI dashboard in Looker Studio containing data from **4,500+ YC-backed startups**, enabling investors to quickly filter by sector, funding stage, and strategic fitment.

---

## 2. Investment Analysis Frameworks

### The Looker Studio Schema for Startup Scoring
When building analytical engines for VC research, compile the following attributes:

| Data Point | Purpose | Sources |
|---|---|---|
| **Funding Velocity** | Speed and frequency of capital raises | Crunchbase / Pitchbook |
| **Team Pedigree** | Past founders, FAANG engineers, elite university grads | LinkedIn API |
| **Moat Score** | Defensibility, active IP, network effects | Patent offices / Github / Product Hunt |
| **Growth Metrics** | Social media traffic growth, active hiring loops | SimilarWeb / LinkedIn jobs |

### Automation of Deal Flow Sourcing
- **Trigger**: New startup enters Y Combinator directory, raises a pre-seed, or submits a pitch deck.
- **Enrichment**: n8n triggers Clay and Apollo API pipelines to enrich founder profiles, company descriptions, and estimated revenues.
- **Filtering**: Script filters candidates against family office criteria (e.g., sector: B2B AI, region: SE Asia, ticket size: $500K-$2M).
- **Matchmaking**: AI generates a draft introduction email summarizing why the startup matches the investor's criteria.
