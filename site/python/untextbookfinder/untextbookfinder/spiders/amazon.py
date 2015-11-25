# amazon.py
#
# Class to retrieve price from Amazon
# Use the following command to call this from PHP where VALUE is <option value="x">:
#   scrapy crawl amazon -a isbn=VALUE
# For example, this is for UNT, FALL 2015, ACCT, 2010, ALL
#   e.g. scrapy crawl amazon -a isbn=9781405182676
#
# Author: Jacob Cole

import json
import urllib2, urllib
import scrapy

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = (
        "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=",
    )

    def __init__(self, isbn):
        self.isbn = isbn

    #encodes as JSON, and dumps for PHP to retrieve
    def dumpAsJsonForPhpCall(self, bookPrice):
        new = bookPrice.rstrip('\r\n')
        result = {'bookPrice': name}
        jsonResult = json.dumps(result).rstrip('\r\n')
        print jsonResult

    #core function. called first when scrapy command is run
    def parse(self, response):
        bookSearchUrl = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=" + self.isbn
        #request url containing the isbn
        return scrapy.Request(bookSearchUrl, callback=self.getBookInfo)

    #extracts price from url
    def getBookInfo(self, response):
        price = response.xpath('//li[@id="result_0"]/div/div/div/div/div/div/div/a/span/text()').extract()

        try:
            self.dumpAsJsonForPhpCall(price[0])
        except IndexError: #if book doesn't exist, it will throw IndexError
            pass

