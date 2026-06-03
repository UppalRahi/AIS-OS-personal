#!/usr/bin/env python3
"""
Filter and Send NRF Exhibitor Leads Batch
----------------------------------------
Filters out Amply, competitors, and corporate tech giants.
Deduplicates delegates by company, choosing the single most senior contact.
Prepares a random batch of 10 leads, exports to CSV, and uploads to Smartlead.
"""

import csv
import os
import sys
import re
import random
import json
import urllib.request
import argparse

INPUT_CSV = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_exhibitors_with_emails.csv'
BATCH_CSV = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/batch_10_leads.csv'
DEFAULT_CAMPAIGN_ID = 3349165  # NRF_Singapore Campaign ID

# Competitor exclusions (including Amply itself)
EXCLUDED_COMPETITORS = {
    'amply', 'getamply', 'yoobic', 'reflexis', 'quinyx', 'zipline', 'storeforce', 
    'simplifield', 'workjam', 'opterus', 'zenput', 'intouch', 'safetyculture', 
    'lumiform', 'gospotcheck', 'field agent', 'fieldagent', 'prontoforms', 
    'truecontext', 'forms on fire', 'formsonfire', 'form.com', 'compli'
}

# Corporate tech giants exclusions
EXCLUDED_GIANTS = {
    'microsoft', 'salesforce', 'google', 'sap', 'oracle', 'amazon', 'ibm', 'accenture', 'workday', 'meta', 'apple'
}

def clean_company_name(name):
    """Cleans company names for professional outreach and metadata matching."""
    if not name:
        return ""
    
    # Remove contents inside parentheses
    name = re.sub(r'\([^)]*\)', '', name).strip()
    
    # Common legal suffixes and branch names
    suffixes = [
        r'\bpte\b\.?', r'\bltd\b\.?', r'\blimited\b', r'\bco\b\.?', r'\bcompany\b', 
        r'\binc\b\.?', r'\bincorporated\b', r'\bcorp\b\.?', r'\bcorporation\b', 
        r'\bpvt\b\.?', r'\bllp\b', r'\bplc\b\.?', r'\bholdings\b', r'\bholding\b', 
        r'\bgroup\b', r'\bsea\b', r'\bsingapore branch\b', r'\bsingapore\b', 
        r'\baustralia\b\.?', r'\bchina\b\.?', r'\bbranch\b',
        r'\bsdn\s*bhd\b\.?', r'\bgmbh\b\.?', r'\bprivate\b\.?', r'\bs\.\s*a\b\.?', r'\bsa\b\.?', r'\baps\b\.?'
    ]
    
    cleaned = name
    for pattern in suffixes:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE).strip()
        
    # Clean up trailing punctuation
    cleaned = re.sub(r'^[,\.\-\s]+|[,\.\-\s]+$', '', cleaned).strip()
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    # Fix all-caps names
    if cleaned.isupper() and len(cleaned) > 3:
        cleaned = cleaned.title()
            
    # Key custom cleanup replacements
    replacements = {
        'Mileapp': 'MileApp',
        'Onebeat': 'OneBeat',
        'Nextscm': 'NextSCM',
        'Xretail': 'XRetail',
        'Fez.': 'Fez',
        'Fez Inc': 'Fez',
        'Fez. Inc': 'Fez',
        'Dentsu Digital': 'Dentsu Digital',
        'Detnsu': 'Dentsu'
    }
    for k, v in replacements.items():
        cleaned = cleaned.replace(k, v)
        
    return cleaned.strip()

def get_domain(email):
    """Extracts email domain."""
    if not email or '@' not in email:
        return ""
    return email.split('@')[1].strip().lower()

def is_excluded(company_name, email):
    """Returns True and the reason if the company or email domain matches exclusions."""
    c_name = company_name.lower()
    dom = get_domain(email)
    
    # Check competitors and Amply
    for comp in EXCLUDED_COMPETITORS:
        if comp in c_name or comp in dom:
            return True, f"Competitor/Amply ({comp})"
            
    # Check giants
    for giant in EXCLUDED_GIANTS:
        if giant in c_name or giant in dom:
            return True, f"Corporate Giant ({giant})"
            
    return False, ""

def score_title(title):
    """Scores a job title's seniority for choosing the single best decision-maker."""
    if not title:
        return 0
    t = title.lower()
    if any(x in t for x in ['founder', 'ceo', 'managing director', 'co-founder', 'owner', 'chairman']):
        return 100
    if any(x in t for x in ['president', 'vp', 'vice president', 'chief', 'director', 'head of', 'head of retail']):
        return 80
    if any(x in t for x in ['manager', 'lead']):
        return 60
    if any(x in t for x in ['specialist', 'engineer', 'analyst', 'account manager']):
        return 40
    return 10

def main():
    parser = argparse.ArgumentParser(description="Filter and batch NRF exhibitor leads.")
    parser.add_argument('--dry-run', action='store_true', help="Run the filter and print selection without sending.")
    parser.add_argument('--send', action='store_true', help="Run the filter and upload selection to Smartlead.")
    args = parser.parse_args()

    # Default to dry-run if neither is specified
    if not args.send and not args.dry_run:
        args.dry_run = True
        print("No action specified. Defaulting to --dry-run mode.\n")

    print("Loading leads from database...")
    if not os.path.exists(INPUT_CSV):
        print(f"Error: Database file not found at {INPUT_CSV}")
        sys.exit(1)

    rows = []
    with open(INPUT_CSV, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    print(f"Total rows in database: {len(rows)}")

    # Keep only rows with successfully generated emails
    processed_rows = [r for r in rows if r.get('email_1_body')]
    print(f"Rows with generated emails: {len(processed_rows)}")

    # Filter and group by company
    companies = {}
    excluded_log = []
    
    for r in processed_rows:
        comp = r.get('company', '').strip()
        email = r.get('Official Email') or r.get('email') or ""
        
        excluded, reason = is_excluded(comp, email)
        if excluded:
            excluded_log.append((comp, email, reason))
            continue

        comp_key = comp.lower().strip()
        if comp_key not in companies:
            companies[comp_key] = []
        companies[comp_key].append(r)

    print(f"Excluded {len(excluded_log)} rows based on competitor/giant filters.")
    print(f"Unique non-excluded companies available: {len(companies)}")

    # For each company, pick the top contact based on seniority score
    selected_delegates = []
    for comp_key, comp_rows in companies.items():
        scored_rows = []
        for r in comp_rows:
            title = r.get('Official Title') or r.get('title') or ""
            score = score_title(title)
            scored_rows.append((score, r))
        
        # Sort descending by score
        scored_rows.sort(key=lambda x: x[0], reverse=True)
        selected_delegates.append(scored_rows[0][1])

    print(f"Deduplicated to {len(selected_delegates)} unique company decision-makers.")

    if len(selected_delegates) < 10:
        print(f"Warning: Only found {len(selected_delegates)} eligible contacts. Preparing a smaller batch.")
        batch_size = len(selected_delegates)
    else:
        batch_size = 10

    # Pick a random 10 companies
    # To make it deterministic for dry-run/testing in the same run, we can seed or just let it be random
    # Let's use a standard random choice
    batch_leads = random.sample(selected_delegates, batch_size)

    # Clean the fields and make them ready
    final_batch = []
    for lead in batch_leads:
        company_raw = lead.get('company', '').strip()
        company_clean = clean_company_name(company_raw)
        
        email = lead.get('Official Email') or lead.get('email') or ""
        first_name = lead.get('firstName', '').strip()
        last_name = lead.get('lastName', '').strip()
        title = lead.get('Official Title') or lead.get('title') or ""
        phone = lead.get('Official Phone') or lead.get('phone') or ""
        
        # Pull generated emails
        email_1_subject = lead.get('email_1_subject', '')
        email_1_body = lead.get('email_1_body', '')
        email_2_subject = lead.get('email_2_subject', '')
        email_2_body = lead.get('email_2_body', '')
        email_3_subject = lead.get('email_3_subject', '')
        email_3_body = lead.get('email_3_body', '')

        # Double check placeholders inside emails. Ensure company name feels natural.
        # Replace placeholders if they refer to raw company names
        email_1_subject = email_1_subject.replace(company_raw, company_clean)
        email_1_body = email_1_body.replace(company_raw, company_clean)
        email_2_subject = email_2_subject.replace(company_raw, company_clean)
        email_2_body = email_2_body.replace(company_raw, company_clean)
        email_3_subject = email_3_subject.replace(company_raw, company_clean)
        email_3_body = email_3_body.replace(company_raw, company_clean)

        final_batch.append({
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'company_name': company_clean,
            'phone_number': phone,
            'website': get_domain(email),
            'custom_fields': {
                'job_title': title,
                'email_1_subject': email_1_subject,
                'email_1_body': email_1_body,
                'email_2_subject': email_2_subject,
                'email_2_body': email_2_body,
                'email_3_subject': email_3_subject,
                'email_3_body': email_3_body
            }
        })

    # Save to BATCH_CSV
    with open(BATCH_CSV, 'w', encoding='utf-8', newline='') as f:
        # Define fieldnames
        fieldnames = ['email', 'first_name', 'last_name', 'company_name', 'phone_number', 'website', 
                      'job_title', 'email_1_subject', 'email_1_body', 'email_2_subject', 'email_2_body', 'email_3_subject', 'email_3_body']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in final_batch:
            flat_item = {
                'email': item['email'],
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'company_name': item['company_name'],
                'phone_number': item['phone_number'],
                'website': item['website'],
                'job_title': item['custom_fields']['job_title'],
                'email_1_subject': item['custom_fields']['email_1_subject'],
                'email_1_body': item['custom_fields']['email_1_body'],
                'email_2_subject': item['custom_fields']['email_2_subject'],
                'email_2_body': item['custom_fields']['email_2_body'],
                'email_3_subject': item['custom_fields']['email_3_subject'],
                'email_3_body': item['custom_fields']['email_3_body'],
            }
            writer.writerow(flat_item)

    print(f"\nSuccessfully prepared batch of {len(final_batch)} leads and saved to {BATCH_CSV}")

    # Display Leads
    print("\n================== BATCH LEADS PREVIEW ==================")
    for idx, lead in enumerate(final_batch):
        print(f"\nLead #{idx+1}:")
        print(f"  Name: {lead['first_name']} {lead['last_name']}")
        print(f"  Title: {lead['custom_fields']['job_title']}")
        print(f"  Company: {lead['company_name']}")
        print(f"  Email: {lead['email']}")
        print(f"  Email 1 Subject: {lead['custom_fields']['email_1_subject']}")
        print("  Email 1 Preview:")
        # Print first few lines of the email
        body_lines = lead['custom_fields']['email_1_body'].split('\n')
        preview_body = '\n'.join(body_lines[:5])
        print(f"    {preview_body.replace(chr(10), chr(10)+'    ')}...")
    print("\n=========================================================")

    if args.dry_run:
        print("\n[DRY RUN COMPLETE] To actually send these leads to Smartlead, run this script with the --send option:")
        print("  python3 send_batch.py --send")
        return

    # Upload flow
    print("\nStarting upload to Smartlead...")
    
    # Retrieve Smartlead API Key
    api_key = os.environ.get('SMARTLEAD_API_KEY')
    if not api_key:
        print("SMARTLEAD_API_KEY environment variable not found.")
        api_key = input("Please enter your Smartlead API Key: ").strip()
        if not api_key:
            print("Error: Smartlead API Key is required to send.")
            sys.exit(1)

    campaign_id_input = input(f"Enter Campaign ID (default: {DEFAULT_CAMPAIGN_ID}): ").strip()
    campaign_id = DEFAULT_CAMPAIGN_ID
    if campaign_id_input:
        try:
            campaign_id = int(campaign_id_input)
        except ValueError:
            print(f"Invalid Campaign ID input. Using default: {DEFAULT_CAMPAIGN_ID}")

    # Prepare payload according to Smartlead requirements
    payload = {
        "lead_list": final_batch,
        "settings": {
            "ignore_global_block_list": False,
            "ignore_unsubscribe_list": False,
            "ignore_community_bounce_list": False,
            "ignore_duplicate_leads_in_other_campaign": False
        }
    }

    url = f"https://api.smartlead.ai/v1/campaigns/{campaign_id}/leads-v2?api_key={api_key}"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )

    try:
        print(f"Uploading {len(final_batch)} leads to Smartlead campaign {campaign_id}...")
        with urllib.request.urlopen(req, timeout=30) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            print("\nUpload Response from Smartlead:")
            print(json.dumps(res_data, indent=2))
            print("\nUpload complete! Batch sent successfully.")
    except Exception as e:
        print(f"\nError uploading to Smartlead: {e}")
        if hasattr(e, 'read'):
            try:
                error_body = e.read().decode('utf-8')
                print(f"Error details: {error_body}")
            except Exception:
                pass
        sys.exit(1)

if __name__ == '__main__':
    main()
