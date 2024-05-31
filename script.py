import os
import time

# Define the arrays for categories, properties, cities, and the range of pages

categories = ['vendre', 'louer']

property_types = ['appartements', 'maisons', 'villas_riad', 'bureaux_et_plateaux', 'magasins_et_commerces']

cities = ['casablanca', 'tanger', 'marrakech', 'fes', 'agadir', 'temara', 'mohammedia', 'sale', 'kenitra', 'rabat', 'oujda', 'el_jadida']  

pages = range(1, 21)  # You can set the range of pages as needed

# Iterate through all combinations of categories, properties, cities, and pages
for category in categories:
    for property in property_types:
        for city in cities:
            for page in pages:
                command = f"scrapy crawl avito_vf -a category={category} -a property={property} -a city={city} -a page={page}"
                # print(f"Executing: {command}")
                os.system(command)
                time.sleep(4)
                #print(category+" "+property+" "+city+" "+str(page))
