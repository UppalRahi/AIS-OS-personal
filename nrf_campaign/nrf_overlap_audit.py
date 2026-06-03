#!/usr/bin/env python3
"""
NRF Lead Overlap Audit Tool
---------------------------
Matches an exhibitor's scanned lead list against the master list of NRF Retailer Delegates.
Generates a custom report of missed retail targets for the exhibitor.
"""

import csv
import sys
import os
import re

MASTER_RETAILERS_CSV = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_retailers.csv'

# Common words to strip when matching company names to reduce false negatives
STOP_WORDS = {
    'ltd', 'limited', 'inc', 'incorporated', 'co', 'company', 'corp', 'corporation',
    'group', 'pte', 'sdn', 'bhd', 'plc', 'holding', 'holdings', 'asia', 'pacific',
    'singapore', 'us', 'usa', 'retail', 'stores', 'supermarket', 'grocer'
}

def clean_company_name(name):
    if not name:
        return ""
    # Lowercase and strip non-alphanumeric chars (keep spaces)
    name_clean = re.sub(r'[^a-zA-Z0-9\s]', '', name.lower())
    # Tokenize and filter out stop words
    tokens = [t for t in name_clean.split() if t not in STOP_WORDS]
    return " ".join(tokens).strip()

def load_master_retailers():
    """Loads master retailers list and indexes them by cleaned company name."""
    if not os.path.exists(MASTER_RETAILERS_CSV):
        print(f"Error: Master retailer list not found at: {MASTER_RETAILERS_CSV}")
        print("Please run segment_nrf_data.py first to generate it.")
        sys.exit(1)

    retailers_by_company = {}
    total_loaded = 0

    with open(MASTER_RETAILERS_CSV, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for row in reader:
            company = row.get('company', '').strip()
            if not company:
                continue
            cleaned = clean_company_name(company)
            if cleaned:
                if cleaned not in retailers_by_company:
                    retailers_by_company[cleaned] = []
                retailers_by_company[cleaned].append(row)
                total_loaded += 1

    print(f"Loaded {total_loaded} retailer delegates across {len(retailers_by_company)} unique brands.")
    return retailers_by_company

def run_audit(scanned_csv_path, output_report_path=None):
    """Compares the scanned leads with the master database and highlights missed opportunities."""
    if not os.path.exists(scanned_csv_path):
        print(f"Error: Scanned leads CSV not found at: {scanned_csv_path}")
        sys.exit(1)

    # 1. Load database
    retailers_db = load_master_retailers()

    # 2. Parse scanned leads
    scanned_companies = set()
    scanned_count = 0
    with open(scanned_csv_path, mode='r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        # Try to find company column
        company_col = None
        for col in reader.fieldnames:
            if 'company' in col.lower() or 'brand' in col.lower() or 'employer' in col.lower():
                company_col = col
                break
        
        if not company_col:
            # Fallback to first column that looks like company
            company_col = reader.fieldnames[4] if len(reader.fieldnames) > 4 else reader.fieldnames[0]
            print(f"Warning: Could not automatically identify company column. Using '{company_col}'")

        for row in reader:
            company = row.get(company_col, '').strip()
            if company:
                cleaned = clean_company_name(company)
                if cleaned:
                    scanned_companies.add(cleaned)
                    scanned_count += 1

    print(f"Parsed {scanned_count} scanned leads from the exhibitor (representing {len(scanned_companies)} unique brands).")

    # 3. Perform matching
    matched_retailer_brands = []
    missed_retailer_brands = []

    for cleaned_brand, delegates in retailers_db.items():
        original_brand_name = delegates[0]['company']
        
        # Check if the exhibitor scanned this brand
        is_matched = False
        for scanned_brand in scanned_companies:
            # Check for exact clean match or substring match to capture variants
            if scanned_brand == cleaned_brand or (len(cleaned_brand) > 3 and cleaned_brand in scanned_brand) or (len(scanned_brand) > 3 and scanned_brand in cleaned_brand):
                is_matched = True
                break
        
        if is_matched:
            matched_retailer_brands.append(original_brand_name)
        else:
            missed_retailer_brands.append((original_brand_name, delegates))

    # 4. Generate Output Report
    if not output_report_path:
        output_report_path = scanned_csv_path.replace('.csv', '_nrf_missed_audit.csv')

    with open(output_report_path, mode='w', encoding='utf-8', newline='') as f:
        # Standard fieldnames for output
        fieldnames = [
            'uID', 'firstName', 'lastName', 'title', 'company', 
            'Official Email', 'Official Phone', 'Official Title', 'Official Country'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        total_delegates_missed = 0
        for brand, delegates in missed_retailer_brands:
            for d in delegates:
                writer.writerow(d)
                total_delegates_missed += 1

    # 5. Display Stats
    total_retailer_brands = len(retailers_db)
    matched_percent = (len(matched_retailer_brands) / total_retailer_brands) * 100 if total_retailer_brands > 0 else 0
    
    print("\n================== NRF AUDIT REPORT ==================")
    print(f"Total Retailer Brands at NRF: {total_retailer_brands}")
    print(f"Exhibitor Scanned Retailer Brands: {len(matched_retailer_brands)} ({matched_percent:.1f}% match rate)")
    print(f"Exhibitor MISSED Retailer Brands: {len(missed_retailer_brands)}")
    print(f"Total Individual Missed Retail Decision-Makers: {total_delegates_missed}")
    print(f"Audit Report Exported to: {output_report_path}")
    print("======================================================")
    print("\nExample missed brands and roles:")
    for i, (brand, delegates) in enumerate(missed_retailer_brands[:10]):
        titles = ", ".join([d.get('title', 'Unknown') for d in delegates[:2]])
        print(f"  - {brand}: {titles}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 nrf_overlap_audit.py <path_to_exhibitor_scanned_leads.csv> [optional_output_path.csv]")
        sys.exit(1)
        
    scanned_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else None
    run_audit(scanned_path, out_path)
