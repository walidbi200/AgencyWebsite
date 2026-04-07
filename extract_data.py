import csv
import json
import os
import re

# We will read 20 valid rows per niche. A valid row has a real email.
niche_paths = {
    'Nursing': r'c:\Users\ZhuFan\Desktop\AgencyWebsite\email_list_2\Pflegefachmann-frau\jobs.csv',
    'IT': r'c:\Users\ZhuFan\Desktop\AgencyWebsite\email_list\Fachinformatiker-in\jobs.csv',
    'Mechatronics': r'c:\Users\ZhuFan\Desktop\AgencyWebsite\email_list\Mechatroniker-in\jobs.csv',
    'Logistics': r'c:\Users\ZhuFan\Desktop\AgencyWebsite\email_list\Fachkraft_fuer_Lagerlogistik\jobs.csv',
    'Gastronomy': r'c:\Users\ZhuFan\Desktop\AgencyWebsite\email_list\Koch-Koechin\jobs.csv'
}

BLACKLISTED_EMAILS = [
    'tcd@a.customvendorconsents',
    'eins@z.du',
    'beratung@ludwig-fresenius.de', # Often generic
]

def clean_location(location, csv_row):
    # Try to find a city name. 
    # Usually in the job_title or job_url or location column
    if not location or location == "N/A":
        # Scrape from job_title if possible (it often has '10367 Berlin' etc)
        title = csv_row.get('job_title', '')
        # Regex for German zip code + city
        match = re.search(r'\b\d{5}\s+([A-Za-zäöüÄÖÜ\s-]+)', title)
        if match:
            return match.group(1).strip()
        return "Deutschland"
        
    # Basic cleanup: take string before comma or space-dash-space
    part = location.split(',')[0].strip()
    # Remove leading zip codes if present
    part = re.sub(r'^\d{5}\s+', '', part)
    return part

def partial_blur_email(email):
    if not email or '@' not in email:
        return email
    parts = email.split('@')
    name_part = parts[0]
    domain_part = parts[1]
    
    if len(name_part) <= 2:
        blurred_name = name_part + '***'
    else:
        blurred_name = name_part[:3] + '***'
        
    return f"{blurred_name}@{domain_part}"

result = {}

for niche_name, csv_path in niche_paths.items():
    data = []
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                email = row.get('email', '').strip()
                if not email or '@' not in email:
                    continue
                
                # Filter blacklisted
                if any(black in email for black in BLACKLISTED_EMAILS):
                    continue
                    
                location = clean_location(row.get('location', ''), row)
                
                data.append({
                    'company': row.get('company', '').strip(),
                    'location': location,
                    'niche': niche_name,
                    'email': partial_blur_email(email),
                    'fullEmail': email 
                })
                count += 1
                if count >= 20:
                    break
    result[niche_name] = data

# Save to JS file
output_path = r'c:\Users\ZhuFan\Desktop\AgencyWebsite\niche_data.js'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('const nicheData = ')
    f.write(json.dumps(result, indent=2, ensure_ascii=False))
    f.write(';')

print(f"Data extracted and saved to {output_path}")
