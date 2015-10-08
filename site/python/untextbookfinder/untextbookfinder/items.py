# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UntextbookfinderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    department = scrapy.Field()
    course = scrapy.Field()
    section = scrapy.Field()
    books = scrapy.Field()
