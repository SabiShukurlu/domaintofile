input_file = r"C:\Users\Admin\Downloads\500domain.txt"
output_file = r"C:\Users\Admin\Downloads\pathdomain.txt"


import requests
import re
import csv
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to check if a domain is a WordPress site
def is_wordpress(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=2)
        if response.status_code == 200:
            content = response.text
            # Check for common WordPress patterns in the HTML content
            if re.search(r'wp-content/themes', content):
                return True
    except requests.RequestException as e:
        logging.warning(f"Request to {domain} failed: {e}")
    return False

# File paths


# Open the input and output files
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    reader = csv.reader(infile)
    total_domains = 0
    wordpress_domains_count = 0

    for row in reader:
        domain = row[1].strip()  # Assuming the domain is in the second column
        total_domains += 1
        if is_wordpress(domain):
            outfile.write(f"{domain}\n")
            wordpress_domains_count += 1
            logging.info(f"WordPress site found: {domain}")

    logging.info(f"Total domains processed: {total_domains}")
    logging.info(f"Total WordPress domains found: {wordpress_domains_count}")

print("WordPress domains have been separated into 'wordpress_domains.txt'.")