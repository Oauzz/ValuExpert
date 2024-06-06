import os
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import time

# Set up argument parser
parser = argparse.ArgumentParser(description="Run Scrapy spider with dynamic page argument.")
parser.add_argument('--page', type=int, required=True, help='End page')

args = parser.parse_args()

# Define the arrays for categories, properties, cities, and the range of pages
categories = ['vendre', 'louer']
property_types = ['appartements', 'maisons', 'villas_riad', 'bureaux_et_plateaux', 'magasins_et_commerces']
cities = ['casablanca', 'tanger', 'marrakech', 'fes', 'agadir', 'temara', 'mohammedia', 'sale', 'kenitra', 'rabat', 'oujda', 'el_jadida']  
end_page = args.page
pages = range(1, end_page+1)  # You can set the range of pages as needed

# Function to run spider with delay and logging
def run_spider(category, property, city, page):
    command = f"scrapy crawl avito_vf -a category={category} -a property={property} -a city={city} -a page={page}"
    subprocess.run(command, shell=True)
    time.sleep(2)  # Add delay between spider runs to avoid overloading the server

with ThreadPoolExecutor(max_workers=5) as executor:  # Control concurrency
    futures = []
    for page in pages:
        for category in categories:
            for property in property_types:
                for city in cities:
                    futures.append(executor.submit(run_spider, category, property, city, page))

    for future in as_completed(futures):
        try:
            future.result()
        except Exception as e:
            print(f"Error running spider: {e}")
