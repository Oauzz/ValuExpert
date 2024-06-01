# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo


class ValueexpPipeline:

    def __init__(self, mongo_uri, mongo_db_rent, mongo_db_sell):
        self.mongo_uri = mongo_uri
        self.mongo_db_rent = mongo_db_rent
        self.mongo_db_sell = mongo_db_sell

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db_rent=crawler.settings.get('MONGO_DB_RENT'),
            mongo_db_sell=crawler.settings.get('MONGO_DB_SELL')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db_rent = self.client[self.mongo_db_rent]
        self.db_sell = self.client[self.mongo_db_sell]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        category = item.get('category')
        property_type = item.get('typee')
        link = item.get('link')
        
        collection_name_map = {
            'appartements': 'appartements',
            'maisons': 'maisons',
            'villas_riad': 'villas',
            'bureaux_et_plateaux': 'bureaux',
            'magasins_et_commerces': 'locaux_commerciaux'
        }

        collection_name = collection_name_map.get(property_type.lower())
        
        if collection_name:
            if category == 'louer':
                collection = self.db_rent[collection_name]
            elif category == 'vendre':
                collection = self.db_sell[collection_name]
            else : 
                return item

            # Check if item with the same link already exists
            if collection.find_one({'link': link}):
                spider.logger.info(f"Duplicate item found: {link}")
            else:
                collection.insert_one(dict(item))
        
        return item
