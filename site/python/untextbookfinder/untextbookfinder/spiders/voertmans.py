# Class to fill out textbook search form for Voertman's
# Use the following command to call this from PHP where VALUE is <option value="x">:
# 	scrapy crawl voertmans -a departmentChoice=VALUE -a courseChoice=VALUE -a sectionChoice=VALUE
# For example, this is for UNT, FALL 2015, ACCT, 2010, ALL
#	e.g. scrapy crawl voertmans -a departmentChoice=198 -a courseChoice=2010 -a sectionChoice=41334
#
# Author: Jacob Cole

import time, json
import urllib2, urllib
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule, CrawlSpider
from selenium import webdriver
from selenium.webdriver.common.by import By

class VoertmansSpider(scrapy.Spider):
	name = "voertmans"
	allowed_domains = ["voertmans.textbooktech.com"]
	start_urls = (
		"http://voertmans.textbooktech.com/textbook",
	)

	def __init__(self, departmentChoice, courseChoice, sectionChoice):
		self.departmentChoice = departmentChoice
		self.courseChoice = courseChoice
		self.sectionChoice = sectionChoice

	def convertToScrapyObject(self, source):
		sou2 = source.encode('ascii','ignore')
		hxs = HtmlXPathSelector(text=sou2)
		return hxs

	def submitForm(self, response):
		driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
		driver.get(response.url)

		#select UNT from dropdown
		schoolOption = driver.find_element_by_xpath("//select[@id='school_selection']/option[@value='6']")
		schoolOption.click()

		driver.implicitly_wait(5)#set to wait for 10 seconds for subsequent element's options to appear

		#select term from dropdown
		termOption = driver.find_element_by_xpath("//select[@id='term_selection']/option[@value='25']")
		termOption.click()

		#select department from dropdown
		departmentOption = driver.find_element_by_xpath(
			"//select[@id='department_selection']/option[@value='" + self.departmentChoice + "']"
		)
		departmentOption.click()

		#select course from dropdown
		courseOption = driver.find_element_by_xpath(
			"//select[@id='course_selection']/option[@value='" + self.courseChoice + "']"
		)
		courseOption.click()

		#select section from dropdown
		sectionOption = driver.find_element_by_xpath(
			"//select[@id='section_selection']/option[@value='" + self.sectionChoice + "']"
		)
		sectionOption.click()

		driver.find_element_by_id("search-button").click()

		time.sleep(5)

		selSource = driver.page_source
		driver.quit()

		return self.convertToScrapyObject(selSource)

	def sendAsPost(self, bookName, bookChoice):
		name = bookName[0].rstrip('\r\n')
		new = bookChoice[0].rstrip('\r\n')
		rental = bookChoice[1].rstrip('\r\n')
		result = {'bookName': name, 'bookNew': new, 'bookRental': rental}
		jsonResult = json.dumps(result).rstrip('\r\n')
		print jsonResult

	def parse(self, response):
		selector = self.submitForm(response)

		bookName = selector.select('//div[@class="book-name"]/text()').extract()
		bookChoice = selector.select('//td[@class="input-box book-choices a-right"]/select/option/text()').extract()

		self.sendAsPost(bookName, bookChoice)
