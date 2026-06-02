# Resource: n8n Playbook

This playbook documents reusable workflow patterns, SQLite data-layer logic, and integration guides for GTM systems.

---

## 1. Core Workflow Principles

### Error Handling & Auto-Retry
- **Pattern**: Every external HTTP/API request should have an Error Trigger or retry configuration set on the node.
- **Rule**: If an API call fails due to rate limits (e.g. 429 errors), implement exponential backoff retry.
- **n8n Setting**: Go to Node Settings -> Enable "Retry On Failure" -> Set Number of Retries (e.g., 3) and Retry Interval (e.g., 5000ms).

### Data Hygiene & Normalization
- **Lead Deduplication**: Never rely solely on CRM deduplication rules. Deduplicate at the data entry gate.
- **State Control**: Use SQLite to track the state of a lead (e.g., `sourcing` -> `enrichment` -> `contacted` -> `replied`).

---

## 2. SQLite Data Layer Snippets

To implement deduplication and state tracking, use these SQL templates inside n8n Execute Query nodes:

### Lead Schema setup
```sql
CREATE TABLE IF NOT EXISTS leads (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT,
    company TEXT,
    linkedin_url TEXT,
    status TEXT DEFAULT 'sourced',
    last_action TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Lead Deduplication & Insertion
```sql
INSERT INTO leads (id, email, first_name, last_name, company, linkedin_url, status)
VALUES ($id, $email, $first_name, $last_name, $company, $linkedin_url, 'sourced')
ON CONFLICT(email) DO UPDATE SET
    updated_at = CURRENT_TIMESTAMP
WHERE status != 'contacted';
```

---

## 3. GTM API Integration Checklist

### Smartlead API
- **Base URL**: `https://api.smartlead.ai/v1`
- **Authentication**: Query parameter `api_key=YOUR_API_KEY`.
- **Common Tasks**:
  - Add leads to campaign: `POST /campaigns/{campaign_id}/leads`
  - Fetch lead message history: `GET /campaigns/{campaign_id}/leads/{email}/message-history`

### Apollo.io API
- **Base URL**: `https://api.apollo.io/v1`
- **Authentication**: Headers `{"Cache-Control": "no-cache", "Content-Type": "application/json"}` with JSON body parameter `api_key`.
- **Common Tasks**:
  - People search: `POST /people/search`
  - Organization search: `POST /organizations/search`

### HubSpot API
- **Base URL**: `https://api.hubapi.com`
- **Authentication**: Header `Authorization: Bearer YOUR_ACCESS_TOKEN`.
- **Common Tasks**:
  - Create contact: `POST /crm/v3/objects/contacts`
  - Update deal stage: `PATCH /crm/v3/objects/deals/{dealId}`
