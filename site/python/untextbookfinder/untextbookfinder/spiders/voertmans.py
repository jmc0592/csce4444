# Class to fill out textbook search form for Voertman's
# Use the following command to call this from PHP where VALUE is <option value="x">:
# 	scrapy crawl voertmans -a departmentChoice=VALUE -a courseChoice=VALUE -a sectionChoice=VALUE
# For example, this is for UNT, FALL 2015, ACCT, 2010, ALL
#	e.g. scrapy crawl voertmans -a departmentChoice=198 -a courseChoice=2010 -a sectionChoice=41334
#
# Author: Jacob Cole

import time#debug
import scrapy
from scrapy.contrib.spiders import Rule, CrawlSpider
from selenium import webdriver
from selenium.webdriver.common.by import By

class VoertmansSpider(scrapy.Spider):
	name = "voertmans"
	allowed_domains = ["voertmans.textbooktech.com"]
	start_urls = (
		"http://voertmans.textbooktech.com/textbook",
	)
	defaultSectionChoice = 41334

	def __init__(self, departmentChoice, courseChoice, sectionChoice):
		self.departmentChoice = departmentChoice
		self.courseChoice = courseChoice
		self.sectionChoice = sectionChoice

	def submitForm(self, response):
		driver = webdriver.Firefox()
		driver.get(response.url)

		#select UNT from dropdown
		schoolOption = driver.find_element_by_xpath("//select[@id='school_selection']/option[@value='6']")
		schoolOption.click()

		driver.implicitly_wait(10)#set to wait for 10 seconds for subsequent element's options to appear

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

		time.sleep(10)#debug
		self.pageSource = driver.page_source

		driver.quit()

	def insertIntoDB():
		pass

	def parse(self, response):
		self.submitForm(response)
		self.insertIntoDB()