# untbookstore.py
#
# Class for scraping all books from the UNT bookstore
# This is only ran to obtain book prices to insert into our database. It will not be ran every time a book is selected. 
#	 So debug statements are okay and helpful if the script fails.
#
# Author: Jacob Cole
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
		self.deptToClick = wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[2]/ul/li["+str(UntbookstoreSpider.globeI+1)+"]")))

		self.deptToClick.click()

		time.sleep(2)   

		self.element_to_hover_over2 = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/input")
		self.hoverCourse = ActionChains(self.driver).move_to_element(self.element_to_hover_over2)
		self.hoverCourse.perform()
		self.element_to_hover_over2.click()

		wait = WebDriverWait(self.driver, 10)
		self.courseToClick = wait.until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[3]/ul/li["+str(UntbookstoreSpider.globeJ+1)+"]")))

		self.courseToClick.click()

		time.sleep(2)   

	def insertIntoParse(self):

		selector = self.convertToScrapyObject(self.driver.page_source)
		bookRequired = selector.select('//div[@class="book-list"]')
		try:
			isbn = bookRequired.select('.//ul/li[3]/text()').extract()
			# for some reason the indexes vary with having the isbn or not. possibly due to white space
			try:
				isbnB = isbn[1].strip()
			except ValueError:
				isbnB = isbn[0].strip()

			print "[Debug][insertIntoParse()]: -----isbn = " + isbnB + "-------"
			name = bookRequired.select('.//h1[@id="skipNavigationToThisElement"]/a/text()').extract()
			nameB = name[0].lstrip()
			nameB2 = nameB.rstrip()
			print "[Debug][insertIntoParse()]: -----name = " + nameB + "------"
			priceNew = bookRequired.select('.//li[@class="selectableBook" and contains(text(), "BUY NEW")]/span/text()').extract()
			priceNewB = priceNew[0].lstrip()
			priceNewB2 = priceNewB.strip()
			priceNewB3 = re.sub('[$]', '', priceNewB2)
			print "[Debug][insertIntoParse()]: -----priceNew = " + priceNewB3 + "------"
			print "[Debug][insertIntoParse()]: ------" + UntbookstoreSpider.BookClass['department'] + " " + UntbookstoreSpider.BookClass['course'] + " " + UntbookstoreSpider.BookClass['section']
			
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
		departments = hxs.select('//div[@class="courseSelectContainer"]/div/div[2]/div/ul/li[2]/ul/li/h4/text()').extract()

		print departments[0] + departments[1] + "-------------------"

		#fill out form with all combinations of choices
		i = 1
		UntbookstoreSpider.globeI = i
		while (i < len(departments)):
			depName = departments[i]
			print "----[Debug]: depName = " + depName + ". i = " + str(i) + "----"
			UntbookstoreSpider.BookClass['department'] = depName
			if(i != 0):
				self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[2]/input").clear()
			#hover and click input element
			self.element_to_hover_over = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[2]/input")
			self.hoverDept = ActionChains(self.driver).move_to_element(self.element_to_hover_over)
			self.hoverDept.perform()
			self.element_to_hover_over.click()

			#click department
			wait = WebDriverWait(self.driver, 10)
			self.deptToClick = wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[2]/ul/li["+str(i+1)+"]")))
			self.deptToClick.click()

			time.sleep(2)

			#obtain course list
			selector = self.convertToScrapyObject(self.driver.page_source)
			courses = selector.select('//div[@class="courseSelectContainer"]/div/div[2]/div/ul/li[3]/ul/li/h4/text()').extract()
			print courses[0] + courses[1] + "-------------------"

			j = 0
			UntbookstoreSpider.globeJ = j
			while (j < len(courses)):
				courseName = courses[j]
				print "----[Debug]: courseName = " + courseName + ". j = " + str(j) +"----"
				UntbookstoreSpider.BookClass['course'] = courseName
				if(j != 0):
					self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/input").clear()
				self.element_to_hover_over2 = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[3]/input")
				self.hoverCourse = ActionChains(self.driver).move_to_element(self.element_to_hover_over2)
				self.hoverCourse.perform()
				self.element_to_hover_over2.click()

				wait = WebDriverWait(self.driver, 10)
				self.courseToClick = wait.until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[3]/ul/li["+str(j+1)+"]")))
				self.courseToClick.click()

				time.sleep(2)

				selector = self.convertToScrapyObject(self.driver.page_source)
				sections = selector.select('//div[@class="courseSelectContainer"]/div/div[2]/div/ul/li[4]/ul/li/h4/text()').extract()
				k = 0
				while (k < len(sections)):
					sectionName = sections[k]
					print "----[Debug]: sectionName = " + sectionName + ". k = " + str(k) +"----"
					UntbookstoreSpider.BookClass['section'] = sectionName
					if(k != 0):
						self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[4]/input[2]").clear()
					self.element_to_hover_over3 = self.driver.find_element_by_xpath("//ul[@class='columnLabelLayout']/li[4]/input[2]")
					self.hoverSection = ActionChains(self.driver).move_to_element(self.element_to_hover_over3)
					self.hoverSection.perform()
					self.element_to_hover_over3.click()

					wait = WebDriverWait(self.driver, 10)
					sectionToClick = wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='columnLabelLayout']/li[4]/ul/li["+str(k+1)+"]")))

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