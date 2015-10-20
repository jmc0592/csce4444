# -*- coding: utf-8 -*-
# Author: Jacob Cole
# Class for scraping all books from the UNT bookstore
import scrapy

class UntbookstoreSpider(scrapy.Spider):
    name = "untbookstore"
    allowed_domains = ["unt.bncollege.com"]
    start_urls = (
    	'http://unt.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=71237',
    )

    def parse(self, response):
        print response.xpath('//li[@class="deptColumn"]/ul').extract()
        '''
        return [scrapy.FormRequest.from_response(
        	response,
            formdata={'data-optionvalue': '66350155', 'age': '27'},
            callback=self.after_post
        )]
        '''
        #possible post request url for department
        #TextBookProcessDropdownsCmd?campusId=57996742&termId=66350155&deptId=66350669&courseId=&sectionId=&storeId=71237&catalogId=10001&langId=-1&dropdown=dept

        #possible post request for course
        #TextBookProcessDropdownsCmd?campusId=57996742&termId=66350155&deptId=66350399&courseId=66354964&sectionId=&storeId=71237&catalogId=10001&langId=-1&dropdown=course
    def after_post(self, response):
    	print "Got to after_post"
    	print response

    #def getAllDepartmentNames():
