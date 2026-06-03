#!/usr/bin/env python3
"""
NRF Enrichment & Outbound Audit Tool
------------------------------------
Selects 10 completely random processed companies from nrf_exhibitors_with_emails.csv,
calls the OpenAI API to score their generated personalization variables and 3-step emails
against our GTM strategy playbook, and outputs a detailed markdown audit report.
"""

import csv
import os
import sys
import random
import json
import urllib.request

INPUT_CSV = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_exhibitors_with_emails.csv'
REPORT_MD = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_enrichment_audit_report.md'

def get_openai_score(api_key, company_name, row_data):
    """Calls OpenAI API to audit and score the generated emails and variables."""
    url = "https://api.openai.com/v1/chat/completions"
    
    audit_payload = {
        "company_name": company_name,
        "product_summary": row_data.get('product_summary', ''),
        "ideal_buyer_titles": row_data.get('ideal_buyer_titles', ''),
        "ideal_buyer_keywords": row_data.get('ideal_buyer_keywords', ''),
        "email_1_subject": row_data.get('email_1_subject', ''),
        "email_1_body": row_data.get('email_1_body', ''),
        "email_2_subject": row_data.get('email_2_subject', ''),
        "email_2_body": row_data.get('email_2_body', ''),
        "email_3_subject": row_data.get('email_3_subject', ''),
        "email_3_body": row_data.get('email_3_body', '')
    }

    prompt = f"""
You are an expert B2B Outbound Campaign Quality Auditor. Your job is to audit the generated outbound messaging data for a company against our strategic playbook rules.

DATA TO AUDIT:
{json.dumps(audit_payload, indent=2)}

SCORING CRITERIA (Score each on a 1-5 scale):
1. **Product Summary Accuracy**: Does the product summary correctly deduce what the company does and start with 'helps retail brands with...' or 'helps retail brands...'?
2. **Email 1 Quality (NRF Hook)**: Does it state they exhibited, explain the 2,428 unique retail delegates walked the floor, state the target count and target brand examples, and end with the soft CTA 'Want me to drop the sample list here?'?
3. **Email 2 Quality (Lead Overlap Match Audit)**: Does it pitch a free Lead Overlap Match Audit (cross-referencing scanned booth leads against the database) and warn them about standard outbound targeting cold lists? Ends with a soft CTA (e.g. 'Would that be helpful...' or 'Open to running the match?').
4. **Email 3 Quality (Outbound Machine Offer)**: Does it offer a fully managed outreach pipeline (n8n + Smartlead) to automate post-event follow-up for missed delegates, include the literal placeholder '[Link to Outbound Workflow Diagram]', and end with the CTA 'Let me know if you want a copy of the workflow template.'?
5. **Tone, Style & Friction**: Is the tone casual, founder-led (Rahi), free of salesy fluff (no 'hope this finds you well'), short-sentenced, and concise?

Output strictly in JSON format matching this schema:
{{
  "product_summary_score": 5,
  "email_1_score": 5,
  "email_2_score": 5,
  "email_3_score": 5,
  "tone_style_score": 5,
  "overall_score": 5.0,
  "qualitative_feedback": "Detailed paragraph explaining the scores, strengths, and any minor alignment issues."
}}
"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4o-mini",
        "response_format": { "type": "json_object" },
        "messages": [
            {"role": "system", "content": "You are a professional B2B cold outreach copy auditor who evaluates email campaigns against structured playbooks."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            content = res_data['choices'][0]['message']['content']
            return json.loads(content)
    except Exception as e:
        print(f"  OpenAI Audit call failed for {company_name}: {e}")
        return None

def main():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not found.")
        sys.exit(1)

    if not os.path.exists(INPUT_CSV):
        print(f"Error: Output file not found at: {INPUT_CSV}")
        sys.exit(1)

    print("Reading and grouping personalized companies from CSV...")
    companies_data = {}
    with open(INPUT_CSV, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            company = row.get('company', '').strip()
            # We want unique companies that have actually been processed
            if company and row.get('email_1_body'):
                company_key = company.lower()
                if company_key not in companies_data:
                    companies_data[company_key] = {
                        'name': company,
                        'data': row
                    }

    processed_companies = list(companies_data.values())
    print(f"Found {len(processed_companies)} unique personalized companies.")
    
    if len(processed_companies) < 10:
        print(f"Warning: Found only {len(processed_companies)} processed companies. Auditing all of them.")
        selected = processed_companies
    else:
        # Seed for randomness but completely random on execution
        selected = random.sample(processed_companies, 10)

    print(f"\nSelected 10 random companies to audit:")
    for idx, c in enumerate(selected):
        print(f"  {idx+1}. {c['name']}")

    audit_results = []
    
    print("\nRunning OpenAI quality audit on each selected company...")
    for idx, c in enumerate(selected):
        print(f"\n[{idx+1}/10] Auditing: {c['name']}")
        audit = get_openai_score(api_key, c['name'], c['data'])
        if audit:
            audit_results.append({
                'company_name': c['name'],
                'scores': audit,
                'data': c['data']
            })
            print(f"  Done. Overall Score: {audit.get('overall_score')}/5")
        else:
            print(f"  Failed auditing {c['name']}.")

    # Generate Markdown Report
    print(f"\nWriting audit report to: {REPORT_MD}")
    
    markdown_content = f"""# NRF Campaign Enrichment Quality Audit Report

This audit evaluates a random sample of 10 companies from the database of {len(processed_companies)} processed exhibitors. The goal is to verify that the generated product summaries and 3-step outbound email sequences align with the GTM strategy playbook.

## 📊 Summary of Audit Scores

| Company Name | Product Summary (1-5) | Email 1: NRF Hook (1-5) | Email 2: Overlap (1-5) | Email 3: Automation (1-5) | Tone & Style (1-5) | Overall Score (1-5) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
"""
    
    sum_product = 0
    sum_e1 = 0
    sum_e2 = 0
    sum_e3 = 0
    sum_tone = 0
    sum_overall = 0
    valid_count = len(audit_results)

    for r in audit_results:
        scores = r['scores']
        markdown_content += f"| **{r['company_name']}** | {scores.get('product_summary_score')} | {scores.get('email_1_score')} | {scores.get('email_2_score')} | {scores.get('email_3_score')} | {scores.get('tone_style_score')} | **{scores.get('overall_score')}** |\n"
        
        sum_product += scores.get('product_summary_score', 0)
        sum_e1 += scores.get('email_1_score', 0)
        sum_e2 += scores.get('email_2_score', 0)
        sum_e3 += scores.get('email_3_score', 0)
        sum_tone += scores.get('tone_style_score', 0)
        sum_overall += scores.get('overall_score', 0)

    if valid_count > 0:
        avg_product = sum_product / valid_count
        avg_e1 = sum_e1 / valid_count
        avg_e2 = sum_e2 / valid_count
        avg_e3 = sum_e3 / valid_count
        avg_tone = sum_tone / valid_count
        avg_overall = sum_overall / valid_count
        
        markdown_content += f"| **AVERAGE** | **{avg_product:.2f}** | **{avg_e1:.2f}** | **{avg_e2:.2f}** | **{avg_e3:.2f}** | **{avg_tone:.2f}** | **{avg_overall:.2f}** |\n"

    markdown_content += "\n---\n\n## 🔍 Company-by-Company Details\n"

    for idx, r in enumerate(audit_results):
        scores = r['scores']
        data = r['data']
        
        markdown_content += f"""
### {idx+1}. {r['company_name']}
* **Overall Quality Score**: {scores.get('overall_score')}/5
* **Product Summary**: *{data.get('product_summary')}*
* **Ideal Buyer Persona**: *{data.get('ideal_buyer_titles')}*

#### ✉️ Generated Copy:
```text
[Email 1]
Subject: {data.get('email_1_subject')}
{data.get('email_1_body')}

[Email 2]
Subject: {data.get('email_2_subject')}
{data.get('email_2_body')}

[Email 3]
Subject: {data.get('email_3_subject')}
{data.get('email_3_body')}
```

#### 📋 Qualitative Feedback:
> {scores.get('qualitative_feedback')}

"""

    with open(REPORT_MD, mode='w', encoding='utf-8') as f_out:
        f_out.write(markdown_content)

    print("\nAudit completed! Report successfully generated.")

if __name__ == '__main__':
    main()
