---
client: PMAPS
project_name: LinkedIn BDR Automation
period: March - April
revenue: ₹30,000
hours_spent: 10
status: Completed
tags: 
  - freelance
  - automation
  - linkedin
  - n8n
  - unipile
---

# Client Project: PMAPS (HR Tech)

## 1. Executive Summary

- **Client Profile**: PMAPS is an HR Tech recruitment platform generating approximately **$2 Million in annual revenue**.
- **Sourcing Strategy**: Acquired during an Answer Engine Optimization (AEO) conference. Discussed GTM solutions with the founder, exchanged contact details, and offered a complimentary 2-3 hour proof-of-concept audit. The high value demonstrated during the trial convinced the founder to sign a paid pilot.
- **Engagement Type**: Paid pilot (goodwill & relationship building).

---

## 2. The Bottleneck (Friction Point)

- **Old Process**: A team of **5 BDRs** was manually running LinkedIn outreach campaigns.
- **Friction**: BDRs had to manually write and send connection requests and follow-up DMs daily.
- **Volume Limit**: Outbound outreach was heavily constrained by human speed, capping daily outbound messages at a maximum of **14 DMs/day** and 50-70 connection requests per BDR.

---

## 3. The Machine (Technical Architecture)

- **Workflow Orchestration**: **n8n** (self-hosted / cloud) orchestrating the campaign logic.
- **Data Layer / Databases**: **Google Sheets** used as a clean CRM frontend for BDRs to track active status.
- **APIs & Tools Integrated**: **Unipile API** used to programmatically send LinkedIn DMs and connection requests directly through BDR accounts.

### Process Map / Logic Flow
1. **Trigger**: New prospect added/approved by BDR in Google Sheets.
2. **Action 1 (Queue & Send)**: n8n fetches pending leads, checks account sending schedules, and calls the Unipile API.
3. **Action 2 (DM/Connection Dispatch)**: Unipile sends programmatic connection requests and sequential follow-up DMs.
4. **Destination**: Google Sheets is updated with delivery status (`Connection Sent`, `Message Sent`, or `Replied`).

---

## 4. The Money (Business Impact & ROI)

- **Outbound Velocity**: Outbound LinkedIn DM operations for all 5 BDRs were fully automated, shifting BDR focus from copy-pasting text to closing warm replies.
- **Time/Cost Savings**: Extremely cost-effective setup for the client. Automated hundreds of manual activities per week.
- **Project Economics**:
  - Total Hours Spent: **10 hours** of high-leverage development.
  - Total Earnings: **₹30,000 INR**
  - Effective Hourly Rate: **₹3,000 / hour**
  - Strategic Outcome: Focus was primarily on long-term goodwill, securing a strong reference from a $2M founder.

---

## 5. High-Leverage Learning / Post-Mortem

- **What worked?**: The "value in advance" strategy (exchanging contacts at a conference and providing a free 2-3 hour audit/pilot) is highly effective for converting B2B founders.
- **Tools**: Unipile combined with n8n proved to be a highly stable, lightweight alternative to expensive enterprise LinkedIn outreach suites.
