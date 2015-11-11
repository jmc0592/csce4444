# -*- coding: utf-8 -*-
# Author: Jacob Cole
# Class for scraping all books from the UNT bookstore
import time, sys, gc
import scrapy
import re
execfile('../../pythonParseConnect.py')
from untextbookfinder.items import UntextbookfinderItem
from parse_rest import *
from parse_rest.query import *
from parse_rest.datatypes import Object
from decimal import *
from scrapy.selector import HtmlXPathSelector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class Book(Object):
    pass

class UntbookstoreSpider(scrapy.Spider):
    name = "untbookstore"
    allowed_domains = ["unt.bncollege.com"]
    start_urls = (
    	'http://unt.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=71237',
    )

    globeI = 0
    globeJ = 0

    BookClass = {'department': '', 'course': '', 'section': ''}

    def convertToScrapyObject(self, source):
        sou2 = source.encode('ascii','ignore')
        hxs = HtmlXPathSelector(text=sou2)
        return hxs

    def refillOutForm(self):
        self.termDropDown = self.driver.find_element_by_xpath("//div[@class='bncbSelectBox termHeader']")
        self.termDropDown.click()

        self.termOption = self.driver.find_element_by_xpath('//li[@class="bncbOptionItem termOption" and text()="FALL 2015"]')
        self.termOption.click()

        self.element_to_hover_over = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[2]/input")
        self.hoverDept = ActionChains(self.driver).move_to_element(self.element_to_hover_over)
        self.hoverDept.perform()
        self.element_to_hover_over.click()

        wait = WebDriverWait(self.driver, 10)
        self.deptToClick = wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[2]/ul/li["+str(UntbookstoreSpider.globeI)+"]")))

        self.deptToClick.click()

        time.sleep(2)   

        self.element_to_hover_over2 = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/input")
        self.hoverCourse = ActionChains(self.driver).move_to_element(self.element_to_hover_over2)
        self.hoverCourse.perform()
        self.element_to_hover_over2.click()

        wait = WebDriverWait(self.driver, 10)
        self.courseToClick = wait.until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[3]/ul/li["+str(UntbookstoreSpider.globeJ)+"]")))

        self.courseToClick.click()

        time.sleep(2)   

    def insertIntoParse(self):
        print "-----page source from insertIntoDb-------"
        selector = self.convertToScrapyObject(self.driver.page_source)
        bookRequired = selector.select('//div[@class="book-list"]')
        isbn = bookRequired.select('.//ul/li[3]/text()').extract()
        isbnB = isbn[1].strip()
        print "Debug: -----isbn = " + isbnB + "-------"
        try:
            name = bookRequired.select('.//h1[@id="skipNavigationToThisElement"]/a/text()').extract()
            nameB = name[0].lstrip()
            nameB2 = nameB.rstrip()
            print "Debug: -----name = " + nameB + "------"
            priceNew = bookRequired.select('.//li[@class="selectableBook" and contains(text(), "BUY NEW")]/span/text()').extract()
            priceNewB = priceNew[0].lstrip()
            priceNewB2 = priceNewB.strip()
            priceNewB3 = re.sub('[$]', '', priceNewB2)
            print "Debug: -----priceNew = " + priceNewB3 + "------"

            try:
                existingBook = Book.Query.get(department=UntbookstoreSpider.BookClass['department'], course=UntbookstoreSpider.BookClass['course'], 
                    section=UntbookstoreSpider.BookClass['section'])
            except QueryResourceDoesNotExist:
                book = Book(isbn=int(isbnB), name=nameB2, priceNew=float(priceNewB3), department=UntbookstoreSpider.BookClass['department'], 
                    course=UntbookstoreSpider.BookClass['course'], section=UntbookstoreSpider.BookClass['section'])
                book.save()
        except IndexError:
            print "Materials pending."

    def parse(self, response):
        self.driver = webdriver.Firefox()
        self.driver.get(response.url)

        self.termDropDown = self.driver.find_element_by_xpath("//div[@class='bncbSelectBox termHeader']")
        self.termDropDown.click()

        self.termOption = self.driver.find_element_by_xpath('//li[@class="bncbOptionItem termOption" and text()="FALL 2015"]')
        self.termOption.click()

        time.sleep(1)


        hxs = self.convertToScrapyObject(self.driver.page_source)
        departments = hxs.select('//li[@class="deptColumn"]/ul/li')

        #fill out form with all combinations of choices
        UntbookstoreSpider.globeI = i = 1
        for i, dep in enumerate(departments):
            depName = dep.xpath('.//text()').extract()
            print "----[Debug]: depName = " + depName[0] + "----"
            UntbookstoreSpider.BookClass['department'] = depName[0]
            if(i != 1):
                self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[2]/input").clear()
            self.element_to_hover_over = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[2]/input")
            self.hoverDept = ActionChains(self.driver).move_to_element(self.element_to_hover_over)
            self.hoverDept.perform()
            self.element_to_hover_over.click()

            wait = WebDriverWait(self.driver, 10)
            self.deptToClick = wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[2]/ul/li["+str(i)+"]")))
            self.deptToClick.click()

            time.sleep(2)

            selector = self.convertToScrapyObject(self.driver.page_source)
            courses = selector.select('//ul[@class="columnLabelLayout"]/li[3]/ul/li')
            UntbookstoreSpider.globeJ = j = 1 #switch back after dept is done
            for j, course in enumerate(courses):
                courseName = course.xpath('.//text()').extract()
                UntbookstoreSpider.BookClass['course'] = courseName[0]
                if(j != 1):
                    self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/input").clear()
                self.element_to_hover_over2 = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/input")
                self.hoverCourse = ActionChains(self.driver).move_to_element(self.element_to_hover_over2)
                self.hoverCourse.perform()
                self.element_to_hover_over2.click()

                wait = WebDriverWait(self.driver, 10)
                self.courseToClick = wait.until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[3]/ul/li["+str(j)+"]")))
                self.courseToClick.click()

                time.sleep(2)

                selector = self.convertToScrapyObject(self.driver.page_source)
                sections = selector.select('//ul[@class="columnLabelLayout"]/li[4]/ul/li')
                k = 1
                for k, section in enumerate(sections):
                    sectionName = section.xpath('.//text()').extract()
                    UntbookstoreSpider.BookClass['section'] = sectionName[0]
                    if(k != 1):
                        self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[4]/input[2]").clear()
                    self.element_to_hover_over3 = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[4]/input[2]")
                    self.hoverSection = ActionChains(self.driver).move_to_element(self.element_to_hover_over3)
                    self.hoverSection.perform()
                    self.element_to_hover_over3.click()

                    wait = WebDriverWait(self.driver, 10)
                    sectionToClick = wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[4]/ul/li["+str(k)+"]")))

                    sectionToClick.click()

                    time.sleep(2)

                    try:
                        submitClick = self.driver.find_element_by_class_name("largeActiveBtn")
                        submitClick.click()
                        time.sleep(3)
                        self.insertIntoParse()
                        self.driver.back()
                        time.sleep(5)
                        self.refillOutForm()
                    except NoSuchElementException:
                        print "No book for this course available."

                    k = k + 1

                j = j + 1
                UntbookstoreSpider.globeJ = j

            i = i + 1
            UntbookstoreSpider.globeI = i

        self.driver.quit()