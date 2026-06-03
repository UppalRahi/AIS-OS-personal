import csv
import os

input_path = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/Global enriched.csv'
exhibitors_output = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_exhibitors_filtered.csv'
retailers_output = '/Users/rahiuppal/Desktop/LIFE/AIS-OS-personal/nrf_campaign/nrf_retailers.csv'

# List of enterprise tech giants to exclude from the exhibitors list
EXCLUDE_GIANTS = [
    'microsoft', 'salesforce', 'sap', 'oracle', 'google', 'amazon', 'aws', 
    'adobe', 'ibm', 'accenture', 'deloitte', 'infosys', 'wipro', 'capgemini', 
    'pwc', 'ey', 'kpmg', 'cisco', 'intel', 'hcl', 'tata', 'tcs', 'cognizant'
]

def segment_data():
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} does not exist.")
        return

    # Ensure output directory exists
    os.makedirs(os.path.dirname(exhibitors_output), exist_ok=True)

    retailers_count = 0
    exhibitors_count = 0
    excluded_count = 0

    with open(input_path, mode='r', encoding='utf-8', errors='ignore') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        with open(exhibitors_output, mode='w', encoding='utf-8', newline='') as exh_file, \
             open(retailers_output, mode='w', encoding='utf-8', newline='') as ret_file:
            
            exh_writer = csv.DictWriter(exh_file, fieldnames=fieldnames)
            ret_writer = csv.DictWriter(ret_file, fieldnames=fieldnames)
            
            exh_writer.writeheader()
            ret_writer.writeheader()

            for row in reader:
                cat = row.get('category', '')
                company = row.get('company', '')

                if cat == 'Delegate (Retailer)':
                    ret_writer.writerow(row)
                    retailers_count += 1
                elif cat == 'Exhibitor':
                    # Check if company is a giant to exclude
                    company_lower = company.lower()
                    is_giant = any(giant in company_lower for giant in EXCLUDE_GIANTS)
                    
                    if is_giant:
                        excluded_count += 1
                    else:
                        exh_writer.writerow(row)
                        exhibitors_count += 1

    print("Data segmentation complete:")
    print(f"  - Retailers exported: {retailers_count}")
    print(f"  - Exhibitors exported: {exhibitors_count} (after excluding {excluded_count} enterprise giants)")
    print(f"  - Retailer file: {retailers_output}")
    print(f"  - Exhibitor file: {exhibitors_output}")

if __name__ == '__main__':
    segment_data()
