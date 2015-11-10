# -*- coding: utf-8 -*-
# Author: Jacob Cole
# Class for scraping all books from the UNT bookstore
import time, sys
import scrapy
from scrapy.selector import HtmlXPathSelector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class UntbookstoreSpider(scrapy.Spider):
    name = "untbookstore"
    allowed_domains = ["unt.bncollege.com"]
    start_urls = (
    	'http://unt.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=71237',
    )

    def convertToScrapyObject(self, source):
        sou2 = source.encode('ascii','ignore')
        hxs = HtmlXPathSelector(text=sou2)
        return hxs

    def fillOutForm(self):
        pass

    def parse(self, response):
        driver = webdriver.Firefox()
        driver.get(response.url)

        termDropDown = driver.find_element_by_xpath("//div[@class='bncbSelectBox termHeader']")
        termDropDown.click()

        termOption = driver.find_element_by_xpath('//li[@class="bncbOptionItem termOption" and text()="FALL 2015"]')
        termOption.click()

        time.sleep(1)

        hxs = self.convertToScrapyObject(driver.page_source)
        departments = hxs.select('//li[@class="deptColumn"]/ul/li')

        #fill out form with all combinations of choices
        i = 1
        for dep in departments:
            depName = dep.xpath('.//text()').extract()
            if(i != 1):
                driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[2]/input").clear()
            element_to_hover_over = driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[2]/input")
            hover = ActionChains(driver).move_to_element(element_to_hover_over)
            hover.perform()
            element_to_hover_over.click()

            time.sleep(2)

            deptToClick = driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[2]/ul/li["+str(i)+"]")
            deptToClick.click()

            time.sleep(2)

            selector = self.convertToScrapyObject(driver.page_source)
            courses = selector.select('//ul[@class="columnLabelLayout"]/li[3]/ul/li')
            j = 1
            for course in courses:
                courseName = course.xpath('.//text()').extract()
                if(j != 1):
                    driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/input").clear()
                element_to_hover_over2 = driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/input")
                hover = ActionChains(driver).move_to_element(element_to_hover_over2)
                hover.perform()
                element_to_hover_over2.click()

                time.sleep(2)

                courseToClick = driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/ul/li["+str(j)+"]")
                courseToClick.click()

                time.sleep(2)

                selector = self.convertToScrapyObject(driver.page_source)
                sections = selector.select('//ul[@class="columnLabelLayout"]/li[4]/ul/li')
                k = 1
                for section in sections:
                    sectionName = section.xpath('.//text()').extract()
                    if(k != 1):
                        driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[4]/input[2]").clear()
                    element_to_hover_over3 = driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[4]/input[2]")
                    hover = ActionChains(driver).move_to_element(element_to_hover_over3)
                    hover.perform()
                    element_to_hover_over3.click()

                    time.sleep(2)

                    sectionToClick = driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[4]/ul/li["+str(k)+"]")
                    sectionToClick.click()

                    time.sleep(2)

                    k = k + 1
                j = j + 1
            i = i + 1
        driver.quit()