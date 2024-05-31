# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ValueexpItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = Field()
    scraped_at = Field()
    list_time = Field()
    link = Field()

    title = Field()

    description = Field()

    area = Field()

    price = Field()

    typee = Field()

    category = Field()

    secondary = Field()


