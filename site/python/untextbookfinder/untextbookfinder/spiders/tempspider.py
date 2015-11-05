import time#debug
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse
from scrapy.contrib.spiders import Rule, CrawlSpider
from selenium import webdriver
from selenium.webdriver.common.by import By

class TempSpider(scrapy.Spider):
	name = "tempspider"
	allowed_domains = ["voertmans.textbooktech.com"]
	start_urls = (
		"http://voertmans.textbooktech.com/textbook",
	)

	def parse(self, response):
		driver = webdriver.Firefox()
		driver.get(response.url)

		#select UNT from dropdown
		schoolOption = driver.find_element_by_xpath("//select[@id='school_selection']/option[@value='6']")
		schoolOption.click()

		driver.implicitly_wait(10)#set to wait for 10 seconds for subsequent element's options to appear

		#select term from dropdown
		termOption = driver.find_element_by_xpath("//select[@id='term_selection']/option[@value='25']")
		termOption.click()
		sou = driver.page_source
        sou2 = sou.encode('ascii','ignore')
        hxs = HtmlXPathSelector(text=sou2)
        departments = hxs.select('//select[@id="department_selection"]/option')

        driver.quit()