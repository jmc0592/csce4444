# -*- coding: utf-8 -*-
import scrapy


class UntbookstoreSpider(scrapy.Spider):
    name = "untbookstore"
    allowed_domains = ["unt.bncollege.com"]
    start_urls = (
    	'http://unt.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=71237',
    )

    def parse(self, response):
        print response.xpath('//li/div/div/ul/li/text()').extract()
        return [scrapy.FormRequest.from_response(
        	response,
            formdata={'data-optionvalue': '66350155', 'age': '27'},
            callback=self.after_post
        )]

    def after_post(self, response):
    	print "Got to after_post"
    	print response