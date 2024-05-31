import os
import time
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Run Scrapy spider with dynamic page argument.")
parser.add_argument('--page', type=int, required=True, help='End page')

args = parser.parse_args()

# Define the arrays for categories, properties, cities, and the range of pages

categories = ['vendre', 'louer']
# categories = ['vendre']


property_types = ['appartements', 'maisons', 'villas_riad', 'bureaux_et_plateaux', 'magasins_et_commerces']

cities = ['casablanca', 'tanger', 'marrakech', 'fes', 'agadir', 'temara', 'mohammedia', 'sale', 'kenitra', 'rabat', 'oujda', 'el_jadida']  

end_page = args.page
pages = range(1, end_page+1)  # You can set the range of pages as needed

# Iterate through all combinations of categories, properties, cities, and pages
for category in categories:
    for property in property_types:
        time.sleep(10)
        for city in cities:
            time.sleep(10)
            for page in pages:
                command = f"scrapy crawl avito_vf -a category={category} -a property={property} -a city={city} -a page={page}"
                # print(f"Executing: {command}")
                os.system(command)
                time.sleep(5)
                #print(category+" "+property+" "+city+" "+str(page))
