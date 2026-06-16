#!/usr/bin/env python3
import csv
import os
import re

# Excluded competitor lists
EXCLUDED_COMPETITORS = {
    'amply', 'getamply', 'yoobic', 'reflexis', 'quinyx', 'zipline', 'storeforce', 
    'simplifield', 'workjam', 'opterus', 'zenput', 'intouch', 'safetyculture', 
    'lumiform', 'gospotcheck', 'field agent', 'fieldagent', 'prontoforms', 
    'truecontext', 'forms on fire', 'formsonfire', 'form.com', 'compli'
}

FILES_TO_CLEAN = [
    '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/Global enriched.csv',
    '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_exhibitors_with_emails.csv',
    '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_exhibitors_filtered.csv',
    '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/batch_10_leads.csv'
]

def get_domain(email):
    if not email or '@' not in email:
        return ""
    return email.split('@')[1].strip().lower()

def is_excluded(company_name, email, country="", official_country=""):
    c_name = company_name.lower()
    dom = get_domain(email)
    
    for comp in EXCLUDED_COMPETITORS:
        # Check if the competitor name is in company name or email domain
        if comp in c_name or comp in dom:
            return True, f"Competitor ({comp})"
            
    if country and 'india' in country.lower():
        return True, "Country is India"
    if official_country and 'india' in official_country.lower():
        return True, "Official Country is India"
        
    return False, ""

def clean_file(file_path):
    if not os.path.exists(file_path):
        print(f"Skipping: {file_path} (does not exist)")
        return
        
    print(f"Cleaning file: {file_path}")
    
    # Read rows
    rows = []
    fieldnames = []
    with open(file_path, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for r in reader:
            rows.append(r)
            
    original_count = len(rows)
    cleaned_rows = []
    removed_count = 0
    
    for r in rows:
        # Find potential company / email / country fields
        company = r.get('company') or r.get('company_name') or r.get('Company') or r.get('Company Name') or ""
        email = r.get('email') or r.get('Official Email') or r.get('Email') or ""
        country = r.get('country') or r.get('Country') or ""
        official_country = r.get('Official Country') or r.get('Official Country') or ""
        
        excluded, matched_reason = is_excluded(company, email, country, official_country)
        if excluded:
            print(f"  Removing: '{company}' | {email} | {country}/{official_country} (matched '{matched_reason}')")
            removed_count += 1
            continue
        cleaned_rows.append(r)
        
    if removed_count > 0:
        # Write back
        with open(file_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(cleaned_rows)
        print(f"  Done. Removed {removed_count} of {original_count} rows.")
    else:
        print("  Done. No matching competitor records found.")

def main():
    print("=========================================================")
    print("        Removing Amply and Competitor Leads             ")
    print("=========================================================\n")
    for f_path in FILES_TO_CLEAN:
        clean_file(f_path)
    print("\nAll files cleaned successfully!")

if __name__ == '__main__':
    main()
