#!/usr/bin/env python3
"""
Clean Existing NRF Exhibitor Emails
-----------------------------------
Retroactively cleans company names (removing legal suffixes like PTE. LTD., CO., LTD.,
fixing all-caps) inside the email subjects and bodies for all already-personalized records
in nrf_exhibitors_with_emails.csv.
"""

import csv
import os
import re

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

def clean_text_replace(text, raw_name, clean_name):
    if not text:
        return ""
        
    # Replace exact raw name case-insensitively (e.g. "DABTON PTE. LTD")
    escaped_raw = re.escape(raw_name)
    text = re.sub(escaped_raw, clean_name, text, flags=re.IGNORECASE)
    
    # Also extract the core name without legal designations to replace separate occurrences
    # e.g., if raw_name is "DABTON PTE. LTD", let's replace "DABTON" (or "Dabton" inside text)
    raw_base = re.sub(r'\([^)]*\)', '', raw_name).strip()
    suffixes = [
        r'\bpte\b\.?', r'\bltd\b\.?', r'\blimited\b', r'\bco\b\.?', r'\bcompany\b', 
        r'\binc\b\.?', r'\bincorporated\b', r'\bcorp\b\.?', r'\bcorporation\b', 
        r'\bpvt\b\.?', r'\bllp\b', r'\bplc\b\.?', r'\bholdings\b', r'\bholding\b', 
        r'\bgroup\b', r'\bsea\b', r'\bsingapore branch\b', r'\bsingapore\b', 
        r'\baustralia\b\.?', r'\bchina\b\.?', r'\bbranch\b'
    ]
    for pattern in suffixes:
        raw_base = re.sub(pattern, '', raw_base, flags=re.IGNORECASE).strip()
    raw_base = re.sub(r'^[,\.\-\s]+|[,\.\-\s]+$', '', raw_base).strip()
    
    if raw_base and len(raw_base) > 3:
        escaped_base = re.escape(raw_base)
        text = re.sub(escaped_base, clean_name, text, flags=re.IGNORECASE)
        
    return text

def main():
    if not os.path.exists(OUTPUT_CSV):
        print(f"Error: Output file not found at: {OUTPUT_CSV}")
        return
        
    print("Reading nrf_exhibitors_with_emails.csv...")
    rows = []
    fieldnames = []
    with open(OUTPUT_CSV, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)
            
    print(f"Loaded {len(rows)} rows. Cleaning company names...")
    cleaned_count = 0
    
    for row in rows:
        company_raw = row.get('company', '').strip()
        if not company_raw:
            continue
            
        company_clean = clean_company_name_for_email(company_raw)
        
        # Replace occurrences in emails if they exist
        email_fields = [
            'email_1_subject', 'email_1_body',
            'email_2_subject', 'email_2_body',
            'email_3_subject', 'email_3_body'
        ]
        
        has_changed = False
        for field in email_fields:
            if field in row and row[field]:
                original = row[field]
                updated = clean_text_replace(original, company_raw, company_clean)
                if updated != original:
                    row[field] = updated
                    has_changed = True
                    
        if has_changed:
            cleaned_count += 1
            
    # Write back
    print(f"Writing {len(rows)} rows back to output CSV (updated emails for {cleaned_count} rows)...")
    with open(OUTPUT_CSV, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
        
    print("Clean-up finished successfully!")

if __name__ == '__main__':
    main()
