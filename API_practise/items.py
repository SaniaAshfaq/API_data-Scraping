# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ApiPractiseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
        id = scrapy.Field()
        name = scrapy.Field()
        symbol  = scrapy.Field()
        slug = scrapy.Field()
        type = scrapy.Field()
        rank = scrapy.Field()
        address  = scrapy.Field()
        search_socre = scrapy.Field()
    
