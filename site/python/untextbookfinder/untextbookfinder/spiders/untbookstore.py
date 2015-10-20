# -*- coding: utf-8 -*-
# Author: Jacob Cole
# Class for scraping all books from the UNT bookstore
import scrapy
from scrapy.selector import HtmlXPathSelector
from selenium import webdriver
from selenium.webdriver.common.by import By

class UntbookstoreSpider(scrapy.Spider):
    name = "untbookstore"
    allowed_domains = ["unt.bncollege.com"]
    start_urls = (
    	'http://unt.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=71237',
    )

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        #get page source ready for selection
        sou=self.driver.page_source
        sou2=sou.encode('ascii','ignore')
        hxs = HtmlXPathSelector(text=sou2)
        #select only the searchFields
        #might have to add the form for POST
        searchFields = hxs.select('//li[@class="deptColumn"]/descendant-or-self::*')
        print searchFields
        '''
        return [scrapy.FormRequest.from_response(
        	response,
            formdata={'data-optionvalue': '66350155', 'age': '27'},
            callback=self.after_post
        )]
        '''
        self.driver.quit()
        #possible post request url for department
        #TextBookProcessDropdownsCmd?campusId=57996742&termId=66350155&deptId=66350669&courseId=&sectionId=&storeId=71237&catalogId=10001&langId=-1&dropdown=dept

        #possible post request for course
        #TextBookProcessDropdownsCmd?campusId=57996742&termId=66350155&deptId=66350399&courseId=66354964&sectionId=&storeId=71237&catalogId=10001&langId=-1&dropdown=course
    def after_post(self, response):
    	print "Got to after_post"
    	print response

    #def getAllDepartmentNames():
