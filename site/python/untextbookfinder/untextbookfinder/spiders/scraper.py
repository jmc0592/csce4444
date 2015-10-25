# -*- coding: utf-8 -*-
import scrapy


class Scraper(scrapy.Spider):
    name = "$scraper"
    allowed_domains = ["$domain"]
    start_urls = (
        'http://www.$domain/',
    )

    def parse(self, response):
        pass

    def getBook():
    	pass
    