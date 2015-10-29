# -*- coding: utf-8 -*-
import scrapy
from parse_rest import *


class Scraper(scrapy.Spider):

    def parse(self, response):
        pass

    def insertIntoDB(self, book):
    	pass

    def checkIfBookExistsInDB(self, isbn):
    	#if book exists
    		#call parse
    	pass
    