

import datetime
import json
import scrapy
from datetime import datetime, timezone
from ValueExp.items import ValueexpItem


class avito_vf(scrapy.Spider):

    name = "avito_vf"
    allowed_domains = ["avito.ma"]
    start_urls = ["https://www.avito.ma/fr"]



    def start_requests(self):
        base_url = 'https://www.avito.ma/fr'
        categories = ['vendre', 'louer']
        # categories = ['vendre']
        property_types = ['appartements', 'maisons', 'villas_riad', 'bureaux_et_plateaux', 'magasins_et_commerces']
        # property_types = ['appartements']
        cities = ['casablanca', 'tanger', 'marrakech', 'fes', 'agadir', 'temara', 'mohammedia', 'sale', 'kenitra', 'rabat', 'oujda', 'el_jadida']  
        # cities = ['rabat']  


        for category in categories:
            for property_type in property_types:
                for city in cities:
                    url = f"{base_url}/{city}/{property_type}-%C3%A0_{category}"
                    yield scrapy.Request(url=url, callback=self.parse_listings, meta={'category': category, 'property_type': property_type, 'city': city})

    def parse_listings(self, response):
            # Extract links to individual item pages
            item_links = response.xpath("//a[contains(@class, 'sc-1jge648-0') and (contains(@class, 'eTbzNs') or contains(@class, 'cEosSi'))]/@href").extract()
            
            for link in item_links:
                if "immoneuf.avito" not in link:
                    yield response.follow(link, self.parse_item, meta=response.meta)
                else :
                    continue
            
            # Handle pagination
            next_page = response.xpath("//a[contains(@class, 'sc-1cf7u6r-0') and contains(@class, 'gRyZxr') and contains(@class, 'sc-2y0ggl-1') and contains(@class, 'yRCEb') and ./div[@style='width:24px;height:24px;background-color:rgba(242, 242, 242,0.2);border-radius:50px']]/@href").get()
            if next_page:
                yield response.follow(next_page, callback=self.parse_listings, meta=response.meta)

    def parse_item(self, response):
        
        script = response.xpath('normalize-space(//script[@id="__NEXT_DATA__"]/text())').get()
        data = json.loads(script)
        dataInfo= data.get('props',{}).get('pageProps',{}).get('componentProps',{}).get('adInfo',{}).get('ad',{})
        
        item = ValueexpItem()
        
        item['city'] = dataInfo.get('location',{}).get('city',{}).get('name') 
        item['list_time'] = dataInfo.get('listTime')
        item['scraped_at'] = datetime.now(timezone.utc).isoformat()
        
        
        item['link'] = dataInfo.get('friendlyUrl',{}).get('url')
        item['title'] = dataInfo.get('subject')
        item['description'] = dataInfo.get('description')
        item['area'] = dataInfo.get('location',{}).get('area',{}).get('name')
        item['price'] = dataInfo.get('price',{}).get('value')
        item['typee'] = response.meta['property_type']  
        item['category'] = response.meta['category']  
        
        # item['typee'] = dataInfo.get('type',{}).get('label')
        # item['category'] = dataInfo.get('category',{}).get('name')
        # item['images'] = dataInfo.get('images',{}) ,

            
        item['secondary'] = self.parse_sec(response,dataInfo)

            
        yield item

    

    def parse_sec(self,response, dataInfo):
        sec={
            'extra':[]
        }
        if(response.meta['property_type']=='appartements'):
            label_to_key = {
                'Âge du bien': 'property_age',
                'Surface habitable': 'habitable_size',
                'Surface totale': 'size',
                'Étage': 'floor',
                'Salons': 'spare_rooms',
                'Chambres': 'rooms',
                'Salle de bain': 'bathrooms'
            }

            boolean_features = {
                'Parking', 'Climatisation', 'Terrasse', 'Sécurité', 'Balcon', 'Ascenseur', 'Meublée', 'Chauffage', 'Cuisine équipée', 'Concierge'
            }

            for category in ['primary', 'secondary']:
                for item in dataInfo['params'][category]:
                    if item['label'] in label_to_key:
                        sec[label_to_key[item['label']]] = item['value']
    
            for item in dataInfo['params']['extra']:
                if item['label'] in boolean_features:
                    sec['extra'].append({item['label']: item['value']})

            # sec={
            #     'property_age' :,
            #     'habitable_size' :,
            #     'size' :,
            #     'floor' :,
            #     'spare_rooms' :,
            #     'rooms' :,
            #     'bathrooms' :,
            #     'extra':[],
            # }
        elif (response.meta['property_type']=='maisons'):


            label_to_key = {
                'Âge du bien': 'property_age',
                'Surface habitable': 'habitable_size',
                'Surface totale': 'size',
                "Nombre d'étage": 'floors',
                'Salons': 'spare_rooms',
                'Chambres': 'rooms',
                'Salle de bain': 'bathrooms'
            }

            boolean_features = {
                'Parking', 'Climatisation', 'Terrasse', 'Sécurité', 'Balcon', 'Garage', 'Meublée', 'Chauffage', 'Cuisine équipée', 'Jardin', 'Piscine'
            }

            for category in ['primary', 'secondary']:
                for item in dataInfo['params'][category]:
                    if item['label'] in label_to_key:
                        sec[label_to_key[item['label']]] = item['value']
    
            for item in dataInfo['params']['extra']:
                if item['label'] in boolean_features:
                    sec['extra'].append({item['label']: item['value']})
            # sec={
            #     'property_age' :,
            #     'habitable_size' :,
            #     'size' :,
            #     'floors' :,
            #     'spare_rooms' :,
            #     'rooms' :,
            #     'bathrooms' :,
            #     'extra':[],
            # }
        elif (response.meta['property_type']=='villas_riad'):

            label_to_key = {
                'Âge du bien': 'property_age',
                'Surface habitable': 'habitable_size',
                'Surface totale': 'size',
                "Nombre d'étage": 'floors',
                'Salons': 'spare_rooms',
                'Chambres': 'rooms',
                'Salle de bain': 'bathrooms'
            }

            boolean_features = {
                'Parking', 'Climatisation', 'Terrasse', 'Sécurité', 'Balcon', 'Garage', 'Meublée', 'Chauffage', 'Cuisine équipée', 'Jardin', 'Piscine'
            }

            for category in ['primary', 'secondary']:
                for item in dataInfo['params'][category]:
                    if item['label'] in label_to_key:
                        sec[label_to_key[item['label']]] = item['value']
    
            for item in dataInfo['params']['extra']:
                if item['label'] in boolean_features:
                    sec['extra'].append({item['label']: item['value']})


            # sec={
            #     'property_age' :,
            #     'habitable_size' :,
            #     'size' :,
            #     'floors' :,
            #     'spare_rooms' :,
            #     'rooms' :,
            #     'bathrooms' :,
            #     'extra':[],
            # }
        elif (response.meta['property_type']=='bureaux_et_plateaux'):

            label_to_key = {
                'Âge du bien': 'property_age',
                'Surface totale': 'size',
                "Étage": 'floor',
                'Nombre de pièces': 'office_units',
                'Salle de bain': 'bathrooms'
            }

            boolean_features = {
                'Parking', 'Climatisation', 'Terrasse', 'Sécurité', 'Ascenseur', 'Chauffage'
            }

            for category in ['primary', 'secondary']:
                for item in dataInfo['params'][category]:
                    if item['label'] in label_to_key:
                        sec[label_to_key[item['label']]] = item['value']
    
            for item in dataInfo['params']['extra']:
                if item['label'] in boolean_features:
                    sec['extra'].append({item['label']: item['value']})


            # sec={
            #     'property_age' :,
            #     'office_units' :,
            #     'size' :,
            #     'floor' :,
            #     'bathrooms' :,
            #     'extra':[],
            # }
        elif (response.meta['property_type']=='magasins_et_commerces'):

            label_to_key = {
                'Âge du bien': 'property_age',
                'Surface totale': 'size',
                'Salle de bain': 'bathrooms'
            }

            boolean_features = {
                'Parking', 'Climatisation', 'Sécurité', 'Chauffage'
            }

            for category in ['primary', 'secondary']:
                for item in dataInfo['params'][category]:
                    if item['label'] in label_to_key:
                        sec[label_to_key[item['label']]] = item['value']
    
            for item in dataInfo['params']['extra']:
                if item['label'] in boolean_features:
                    sec['extra'].append({item['label']: item['value']})


            # sec={
            #     'property_age' :,
            #     'size' :,
            #     'bathrooms' :,
            #     'extra':[],
            # }
        return sec



        
