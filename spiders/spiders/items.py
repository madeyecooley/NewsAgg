# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    Title = scrapy.Field()
    URL = scrapy.Field()
    Author = scrapy.Field()
    Summary = scrapy.Field()
    Photo = scrapy.Field()
    Credit_Caption = scrapy.Field()
    Site = scrapy.Field()
