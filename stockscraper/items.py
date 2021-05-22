# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockscraperItem(scrapy.Item):
    # define the fields for your item here like:
    low_price = scrapy.Field()
    high_price = scrapy.Field()
    date = scrapy.Field()
    volume = scrapy.Field()
    current_price = scrapy.Field()
    pass
