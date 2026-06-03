#!/usr/bin/env python3
"""
NRF Outbound Generator
----------------------
Scrapes exhibitor homepages, queries the local NRF retailer database to match target niches,
and calls the OpenAI API to draft hyper-personalized 3-step email sequences.
"""

import csv
import os
import sys
import re
import json
import ssl
import urllib.request

EXHIBITORS_CSV = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_exhibitors_filtered.csv'
RETAILERS_CSV = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_retailers.csv'
OUTPUT_CSV = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_exhibitors_with_emails.csv'

def clean_company_name_for_email(name):
    """
    Cleans raw company names to sound human-written in email copy.
    Removes legal designations, branch locations, and fixes ALL-CAPS names.
    """
    if not name:
        return ""
    
    # Remove contents inside parentheses
    name = re.sub(r'\([^)]*\)', '', name).strip()
    
    # Common legal designations and branch names
    suffixes = [
        r'\bpte\b\.?', r'\bltd\b\.?', r'\blimited\b', r'\bco\b\.?', r'\bcompany\b', 
        r'\binc\b\.?', r'\bincorporated\b', r'\bcorp\b\.?', r'\bcorporation\b', 
        r'\bpvt\b\.?', r'\bllp\b', r'\bplc\b\.?', r'\bholdings\b', r'\bholding\b', 
        r'\bgroup\b', r'\bsea\b', r'\bsingapore branch\b', r'\bsingapore\b', 
        r'\baustralia\b\.?', r'\bchina\b\.?', r'\bbranch\b'
    ]
    
    cleaned = name
    for pattern in suffixes:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE).strip()
        
    # Clean up trailing punctuation
    cleaned = re.sub(r'^[,\.\-\s]+|[,\.\-\s]+$', '', cleaned).strip()
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    # Title Case if all uppercase and length > 3
    if cleaned.isupper():
        if len(cleaned) <= 3:
            pass
        else:
            cleaned = cleaned.title()
            
    # Key replacements
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

def clean_domain(email):
    """Extracts domain from email address."""
    if not email or '@' not in email:
        return ""
    domain = email.split('@')[1].strip().lower()
    # Skip common generic email domains
    generic_domains = {'gmail.com', 'outlook.com', 'yahoo.com', 'hotmail.com', 'icloud.com', 'protonmail.com'}
    if domain in generic_domains:
        return ""
    return domain

def scrape_homepage(domain):
    """Scrapes homepage content using standard library urllib."""
    url = f"https://{domain}"
    print(f"Scraping: {url}...")
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as response:
            html = response.read().decode('utf-8', errors='ignore')
            # Remove scripts and style sections
            html = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', html, flags=re.IGNORECASE)
            html = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', html, flags=re.IGNORECASE)
            # Remove all HTML tags
            text = re.sub(r'<[^>]+>', ' ', html)
            # Normalize whitespaces
            text = ' '.join(text.split())
            return text[:3000] # Return first 3,000 characters
    except Exception as e:
        print(f"  Scrape failed for {url} (Error: {e}). Trying http...")
        # Fallback to http
        try:
            url_http = f"http://{domain}"
            req = urllib.request.Request(url_http, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=8) as response:
                html = response.read().decode('utf-8', errors='ignore')
                html = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', html, flags=re.IGNORECASE)
                html = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', html, flags=re.IGNORECASE)
                text = re.sub(r'<[^>]+>', ' ', html)
                text = ' '.join(text.split())
                return text[:3000]
        except Exception as e2:
            print(f"  HTTP Scrape failed too: {e2}")
            return ""

def find_matching_retailers(keywords):
    """Scans the local nrf_retailers.csv and returns counts & examples matching keywords."""
    if not os.path.exists(RETAILERS_CSV):
        return 0, ["FairPrice Group", "Sephora"]

    matching_leads = []
    # clean keywords
    kw_list = [k.strip().lower() for k in keywords.split(',') if k.strip()]
    
    with open(RETAILERS_CSV, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get('title', '').lower()
            company = row.get('company', '').strip()
            
            # Check if any keyword matches the title
            is_match = any(kw in title for kw in kw_list)
            if is_match and company:
                matching_leads.append(row)

    count = len(matching_leads)
    unique_companies = list(set([l['company'] for l in matching_leads]))
    # Fallback default if not enough unique examples
    if len(unique_companies) < 2:
        unique_companies.extend(["FairPrice Group", "Sephora"])
    
    examples = unique_companies[:2]
    return count, examples

def classify_exhibitor_buyer(api_key, company_name, site_text):
    """Calls OpenAI API to classify product and identify ideal buyer keywords."""
    url = "https://api.openai.com/v1/chat/completions"
    
    prompt = f"""
Analyze the following homepage text of the company '{company_name}' who exhibited at the NRF retail trade show.
Determine what they sell to retailers, their value proposition, and the job titles they target in retail.

HOMEPAGE COPY SEGMENT:
\"\"\"
{site_text}
\"\"\"

Output strictly in JSON format matching this schema:
{{
  "product_summary": "value proposition starting with 'helps retail brands with...'",
  "ideal_buyer_titles": "ideal retail job titles/departments they target, e.g. 'supply chain and logistics'",
  "ideal_buyer_keywords": "comma-separated keywords to query in our retailer database to find matching titles, e.g. 'supply,logistics,delivery,procurement'"
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
            {"role": "system", "content": "You are a GTM Engineering assistant who classifies retail tech products and targets."},
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
        print(f"  OpenAI Classification failed: {e}")
        return None

def generate_openai_emails(api_key, company_name, count, examples, classification):
    """Calls OpenAI API to draft the personalized outbound emails using NRF database match details."""
    url = "https://api.openai.com/v1/chat/completions"
    
    product_summary = classification.get('product_summary', 'helps retail brands optimize operations')
    ideal_buyer_titles = classification.get('ideal_buyer_titles', 'retail technology and operations')
    
    prompt = f"""
Draft a 3-step outbound email campaign from Rahi (B2B GTM Specialist) targeting '{company_name}', who exhibited at NRF.
We are selling them our NRF Retailer Delegate data service.

EXHIBITOR INTELLIGENCE:
* Company Name: {company_name}
* Product Summary: {product_summary}
* Target Buyer Persona: {ideal_buyer_titles}

REAL NRF DATABASE MATCH DATA:
* Target Count: We found {count} retail delegates matching their buyer persona in our NRF attendee database.
* Sample target retail brands in our list: {examples[0]} and {examples[1]}.

You MUST construct the 3 emails strictly according to the following strategic playbook templates:

### Email 1: The Site-Scraped NRF Hook
* Goal: Show that you understand exactly what they sell and offer a custom, highly relevant slice of the NRF list.
* Subject: NRF follow-up gap for {company_name}
* Structure:
  Hi [First Name],

  I saw you were exhibiting at NRF Singapore this year.

  Since {company_name} {product_summary}, I assume your sales team was walking the floor looking to connect with {ideal_buyer_titles} decision-makers.

  While you likely scanned a few badges, NRF had 2,428 unique retail delegates walking the floor—most of whom bypass booths.

  I ran a query on our verified database of delegates and mapped {count} active {ideal_buyer_titles} leads who attended, including decision-makers from brands like {examples[0]} and {examples[1]}.

  I put together a quick 3-column sheet with 5 verified contacts matching your target profile so your team can test the data quality.

  Want me to drop the sample list here?

  Best,
  Rahi

### Email 2: The Competitive Match / Lead Overlap Match Audit Play
* Goal: Pitch a free Lead Overlap Match Audit. Focus on the fact that post-event outreach usually targets generic cold lists, but physical NRF attendees are warm.
* Subject: missing {ideal_buyer_titles} leads from NRF
* Structure:
  Hi [First Name],

  Following up on my last note.

  When sales teams follow up after NRF, they usually run generic outbound targeting cold databases. But the fact that retail decision-makers from brands like {examples[0]} and {examples[1]} physically attended NRF makes them highly warm accounts.

  I set up a targeted slice of the NRF database containing only the {count} {ideal_buyer_titles} delegates.

  If you want to send over a list of the companies your reps scanned at the show, I can run a quick check against our database to show you exactly which matching retail targets walked past your booth without scanning.

  Would that be helpful for your sales team?

  Best,
  Rahi

### Email 3: The Outbound Campaign Offer
* Goal: Shift from selling raw datasets to offering a done-for-you outreach pipeline/machine setup (using n8n + Smartlead).
* Subject: outbound pipeline for {company_name}'s NRF data
* Structure:
  Hi [First Name],

  Since I haven't heard back, I'm assuming your sales reps are fully occupied following up on the badges they scanned.

  Beyond just selling raw datasets, we build automated, multi-channel GTM pipelines (using n8n and Smartlead) to reach NRF delegates.

  Instead of your team manually writing emails, I can set up an automated sequence that reaches the exact {count} {ideal_buyer_titles} prospects you missed, mentioning their NRF attendance to schedule post-event demos.

  I put together a quick diagram of how this outbound machine is structured:

  [Link to Outbound Workflow Diagram]

  Let me know if you want a copy of the workflow template.

  Best,
  Rahi

Requirements for all draft bodies:
- Keep the style professional yet casual, founder-led (Rahi). Do not add any corporate or salesy fluff (like "hope this email finds you well" or "let's book a 15-minute call").
- Incorporate the exact count of {count} and the target brands ({examples[0]} and {examples[1]}) naturally.
- Keep emails concise (under 120 words each).
- Make sure to use the exact subject lines requested in the output schema.
- Use "[First Name]" as the placeholder for the recipient's first name.

Output strictly in JSON format matching this schema:
{{
  "email_1_subject": "NRF follow-up gap for {company_name}",
  "email_1_body": "Full body text of email 1",
  "email_2_subject": "missing {ideal_buyer_titles} leads from NRF",
  "email_2_body": "Full body text of email 2",
  "email_3_subject": "outbound pipeline for {company_name}'s NRF data",
  "email_3_body": "Full body text of email 3"
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
            {"role": "system", "content": "You are a GTM Engineering copywriter who writes high-conversion outbound email campaigns."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            content = res_data['choices'][0]['message']['content']
            return json.loads(content)
    except Exception as e:
        print(f"  OpenAI Email Draft failed: {e}")
        return None


def main():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        api_key = input("Enter your OpenAI API Key: ").strip()
        if not api_key:
            print("Error: OpenAI API Key is required.")
            sys.exit(1)

    print("Checking database files...")
    if not os.path.exists(EXHIBITORS_CSV):
        print(f"Error: Exhibitors list not found at {EXHIBITORS_CSV}")
        sys.exit(1)

    # Group by company name (lowercased to normalize names like ETP International)
    all_rows = []
    with open(EXHIBITORS_CSV, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            all_rows.append(row)

    companies_map = {}
    for row in all_rows:
        company_raw = row.get('company', '').strip()
        if not company_raw:
            continue
        company_clean = company_raw.lower()
        if company_clean not in companies_map:
            companies_map[company_clean] = {
                'name_display': company_raw,
                'rows': []
            }
        companies_map[company_clean]['rows'].append(row)

    unique_companies_keys = list(companies_map.keys())

    # Ask how many unique companies to process (default 5 for testing)
    limit_str = input("How many unique companies would you like to process? (default 5, enter 'all' for entire list): ").strip()
    limit = 5
    if limit_str.lower() == 'all':
        limit = None
    elif limit_str.isdigit():
        limit = int(limit_str)

    if limit:
        unique_companies_keys = unique_companies_keys[:limit]

    output_fieldnames = fieldnames + [
        'product_summary', 'ideal_buyer_titles', 'ideal_buyer_keywords',
        'email_1_subject', 'email_1_body', 
        'email_2_subject', 'email_2_body', 
        'email_3_subject', 'email_3_body'
    ]

    # Load already processed companies if output file exists
    processed_cache = {}
    if os.path.exists(OUTPUT_CSV):
        try:
            with open(OUTPUT_CSV, mode='r', encoding='utf-8', errors='ignore') as f_read:
                reader = csv.DictReader(f_read)
                for row in reader:
                    comp_name = row.get('company', '').strip()
                    if not comp_name:
                        continue
                    comp_clean = comp_name.lower()
                    # Check if it was successfully processed (has email body)
                    if row.get('email_1_body'):
                        processed_cache[comp_clean] = {
                            'product_summary': row.get('product_summary', ''),
                            'ideal_buyer_titles': row.get('ideal_buyer_titles', ''),
                            'ideal_buyer_keywords': row.get('ideal_buyer_keywords', ''),
                            'email_1_subject': row.get('email_1_subject', ''),
                            'email_1_body': row.get('email_1_body', ''),
                            'email_2_subject': row.get('email_2_subject', ''),
                            'email_2_body': row.get('email_2_body', ''),
                            'email_3_subject': row.get('email_3_subject', ''),
                            'email_3_body': row.get('email_3_body', '')
                        }
            print(f"Loaded {len(processed_cache)} already processed companies from existing output file.")
        except Exception as e:
            print(f"Warning: Could not read existing output file for cache: {e}")

    print(f"Starting pipeline for {len(unique_companies_keys)} unique companies...")
    
    with open(OUTPUT_CSV, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=output_fieldnames, extrasaction='ignore')
        writer.writeheader()

        for idx, comp_key in enumerate(unique_companies_keys):
            comp_info = companies_map[comp_key]
            company_name = comp_info['name_display']
            rows = comp_info['rows']
            
            print(f"\n[{idx+1}/{len(unique_companies_keys)}] Processing Company: {company_name} ({len(rows)} delegates)")
            
            personalization = {}
            if comp_key in processed_cache:
                print(f"  [CACHE HIT] Already processed. Loading emails from existing output CSV.")
                personalization = processed_cache[comp_key]
            else:
                # Find first available domain
                domain = ""
                for r in rows:
                    email = r.get('Official Email', '')
                    d = clean_domain(email)
                    if d:
                        domain = d
                        break
                
                site_text = ""
                if domain:
                    site_text = scrape_homepage(domain)
                
                # Default lookup keywords based on company name/email domains
                default_kws = "it,technology,marketing,supply,logistics,operations,pos,retail"
                count, examples = find_matching_retailers(default_kws)
                
                company_name_clean = clean_company_name_for_email(company_name)
                
                if site_text:
                    # Step 1: Classify and get ideal keywords
                    classification = classify_exhibitor_buyer(api_key, company_name_clean, site_text)
                    if classification:
                        # Step 2: Query database with actual keywords
                        keywords = classification.get('ideal_buyer_keywords', 'retail')
                        count, examples = find_matching_retailers(keywords)
                        
                        # Step 3: Generate the personalized emails
                        generated = generate_openai_emails(api_key, company_name_clean, count, examples, classification)
                        if generated:
                            # Combine classification info and emails
                            personalization.update(classification)
                            personalization.update(generated)
                            print(f"  Successfully personalized emails for {company_name_clean} using GPT (found {count} matching leads!).")
                        else:
                            print(f"  Failed generating emails. Fallback for {company_name_clean}.")
                            fallback_ps = classification.get('product_summary', 'helps retail brands automate operations')
                            fallback_ibt = classification.get('ideal_buyer_titles', 'operations and IT')
                            personalization = {
                                'product_summary': fallback_ps,
                                'ideal_buyer_titles': fallback_ibt,
                                'email_1_subject': f"NRF follow-up gap for {company_name_clean}",
                                'email_1_body': (
                                    f"Hi [First Name],\n\n"
                                    f"I saw you were exhibiting at NRF Singapore this year.\n\n"
                                    f"Since {company_name_clean} {fallback_ps}, I assume your sales team was walking the floor looking to connect with {fallback_ibt} decision-makers.\n\n"
                                    f"While you likely scanned a few badges, NRF had 2,428 unique retail delegates walking the floor—most of whom bypass booths.\n\n"
                                    f"I ran a query on our verified database of delegates and mapped {count} active {fallback_ibt} leads who attended the show, including decision-makers from brands like {examples[0]} and {examples[1]}.\n\n"
                                    f"I put together a quick 3-column sheet with 5 verified contacts matching your target profile so your team can test the data quality.\n\n"
                                    f"Want me to drop the sample list here?\n\n"
                                    f"Best,\n"
                                    f"Rahi"
                                ),
                                'email_2_subject': f"missing {fallback_ibt} leads from NRF",
                                'email_2_body': (
                                    f"Hi [First Name],\n\n"
                                    f"Following up on my last note.\n\n"
                                    f"When sales teams follow up after NRF, they usually run generic outbound targeting cold databases. But the fact that retail decision-makers from brands like {examples[0]} and {examples[1]} physically attended NRF makes them highly warm accounts.\n\n"
                                    f"I set up a targeted slice of the NRF database containing only the {count} {fallback_ibt} delegates.\n\n"
                                    f"If you want to send over a list of the companies your reps scanned at the show, I can run a quick check against our database to show you exactly which matching retail targets walked past your booth without scanning.\n\n"
                                    f"Would that be helpful for your sales team?\n\n"
                                    f"Best,\n"
                                    f"Rahi"
                                ),
                                'email_3_subject': f"outbound pipeline for {company_name_clean}'s NRF data",
                                'email_3_body': (
                                    f"Hi [First Name],\n\n"
                                    f"Since I haven't heard back, I'm assuming your sales reps are fully occupied following up on the badges they scanned.\n\n"
                                    f"Beyond just selling raw datasets, we build automated, multi-channel GTM pipelines (using n8n and Smartlead) to reach NRF delegates.\n\n"
                                    f"Instead of your team manually writing emails, I can set up an automated sequence that reaches the exact {count} {fallback_ibt} prospects you missed, mentioning their NRF attendance to schedule post-event demos.\n\n"
                                    f"I put together a quick diagram of how this outbound machine is structured:\n\n"
                                    f"[Link to Outbound Workflow Diagram]\n\n"
                                    f"Let me know if you want a copy of the workflow template.\n\n"
                                    f"Best,\n"
                                    f"Rahi"
                                )
                            }
                    else:
                        print(f"  Failed classifying. Fallback for {company_name_clean}.")
                        personalization = {
                            'product_summary': "helps retail brands automate operations",
                            'ideal_buyer_titles': "operations and IT",
                            'email_1_subject': f"NRF follow-up gap for {company_name_clean}",
                            'email_1_body': (
                                f"Hi [First Name],\n\n"
                                f"I saw you were exhibiting at NRF Singapore this year.\n\n"
                                f"Since {company_name_clean} helps retail brands automate operations, I assume your sales team was walking the floor looking to connect with operations and IT decision-makers.\n\n"
                                f"While you likely scanned a few badges, NRF had 2,428 unique retail delegates walking the floor—most of whom bypass booths.\n\n"
                                f"I ran a query on our verified database of delegates and mapped {count} active operations and IT leads who attended the show, including decision-makers from brands like {examples[0]} and {examples[1]}.\n\n"
                                f"I put together a quick 3-column sheet with 5 verified contacts matching your target profile so your team can test the data quality.\n\n"
                                f"Want me to drop the sample list here?\n\n"
                                f"Best,\n"
                                f"Rahi"
                            ),
                            'email_2_subject': "missing operations and IT leads from NRF",
                            'email_2_body': (
                                f"Hi [First Name],\n\n"
                                f"Following up on my last note.\n\n"
                                f"When sales teams follow up after NRF, they usually run generic outbound targeting cold databases. But the fact that retail decision-makers from brands like {examples[0]} and {examples[1]} physically attended NRF makes them highly warm accounts.\n\n"
                                f"I set up a targeted slice of the NRF database containing only the {count} operations and IT delegates.\n\n"
                                f"If you want to send over a list of the companies your reps scanned at the show, I can run a check against our database to show you exactly which matching retail targets walked past your booth without scanning.\n\n"
                                f"Would that be helpful for your sales team?\n\n"
                                f"Best,\n"
                                f"Rahi"
                            ),
                            'email_3_subject': f"outbound pipeline for {company_name_clean}'s NRF data",
                            'email_3_body': (
                                f"Hi [First Name],\n\n"
                                f"Since I haven't heard back, I'm assuming your sales reps are fully occupied following up on the badges they scanned.\n\n"
                                f"Beyond just selling raw datasets, we build automated, multi-channel GTM pipelines (using n8n and Smartlead) to reach NRF delegates.\n\n"
                                f"Instead of your team manually writing emails, I can set up an automated sequence that reaches the exact {count} operations and IT prospects you missed, mentioning their NRF attendance to schedule post-event demos.\n\n"
                                f"I put together a quick diagram of how this outbound machine is structured:\n\n"
                                f"[Link to Outbound Workflow Diagram]\n\n"
                                f"Let me know if you want a copy of the workflow template.\n\n"
                                f"Best,\n"
                                f"Rahi"
                            )
                        }
                else:
                    print(f"  No website text scraped. Writing default template for {company_name_clean}.")
                    default_kws = "it,technology,marketing,supply,logistics,operations,pos,retail"
                    count, examples = find_matching_retailers(default_kws)
                    personalization = {
                        'product_summary': "helps retail brands with operations and tech",
                        'ideal_buyer_titles': "retail technology and operations",
                        'email_1_subject': f"NRF follow-up gap for {company_name_clean}",
                        'email_1_body': (
                            f"Hi [First Name],\n\n"
                            f"I saw you were exhibiting at NRF Singapore this year.\n\n"
                            f"Since {company_name_clean} helps retail brands with operations and tech, I assume your sales team was walking the floor looking to meet retail technology and operations decision-makers.\n\n"
                            f"While you likely scanned a few badges, NRF had 2,428 unique retail delegates walking the floor—most of whom bypass booths.\n\n"
                            f"I ran a query on our verified database of delegates and mapped {count} active retail technology and operations leads who attended the show, including decision-makers from brands like {examples[0]} and {examples[1]}.\n\n"
                            f"I put together a quick 3-column sheet with 5 verified contacts matching your target profile so your team can test the data quality.\n\n"
                            f"Want me to drop the sample list here?\n\n"
                            f"Best,\n"
                            f"Rahi"
                        ),
                        'email_2_subject': "missing retail technology leads from NRF",
                        'email_2_body': (
                            f"Hi [First Name],\n\n"
                            f"Following up on my last note.\n\n"
                            f"When sales teams follow up after NRF, they usually run generic outbound targeting cold databases. But the fact that retail decision-makers from brands like {examples[0]} and {examples[1]} physically attended NRF makes them highly warm accounts.\n\n"
                            f"I set up a targeted slice of the NRF database containing only the {count} retail technology and operations delegates.\n\n"
                            f"If you want to send over a list of the companies your reps scanned at the show, I can run a quick check against our database to show you exactly which matching retail targets walked past your booth without scanning.\n\n"
                            f"Would that be helpful for your sales team?\n\n"
                            f"Best,\n"
                            f"Rahi"
                        ),
                        'email_3_subject': f"outbound pipeline for {company_name_clean}'s NRF data",
                        'email_3_body': (
                            f"Hi [First Name],\n\n"
                            f"Since I haven't heard back, I'm assuming your sales reps are fully occupied following up on the badges they scanned.\n\n"
                            f"Beyond just selling raw datasets, we build automated, multi-channel GTM pipelines (using n8n and Smartlead) to reach NRF delegates.\n\n"
                            f"Instead of your team manually writing emails, I can set up an automated sequence that reaches the exact {count} retail technology prospects you missed, mentioning their NRF attendance to schedule post-event demos.\n\n"
                            f"I put together a quick diagram of how this outbound machine is structured:\n\n"
                            f"[Link to Outbound Workflow Diagram]\n\n"
                            f"Let me know if you want a copy of the workflow template.\n\n"
                            f"Best,\n"
                            f"Rahi"
                        )
                    }
                
            # Apply same personalization to all delegate rows for this company and write
            for r in rows:
                r.update(personalization)
                writer.writerow(r)
            
    print(f"\nPipeline finished! Output saved to: {OUTPUT_CSV}")

if __name__ == '__main__':
    main()

