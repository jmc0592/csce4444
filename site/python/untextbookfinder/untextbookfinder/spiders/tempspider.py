import time#debug
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By

class TempSpider(scrapy.Spider):
    name = "tempspider"
    allowed_domains = ["voertmans.textbooktech.com"]
    start_urls = (
        "http://voertmans.textbooktech.com/textbook",
    )

    def convertToScrapyObject(self, source):
        sou2 = source.encode('ascii','ignore')
        hxs = HtmlXPathSelector(text=sou2)
        return hxs

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

        time.sleep(3)
            
        sou = driver.page_source
        sou2 = sou.encode('ascii','ignore')
        hxs = HtmlXPathSelector(text=sou2)
        departments = hxs.select('//select[@id="department_selection"]/option')

        myfile = open("options.txt", "a")

        #loop through each department to get each course
        for dep in departments:
            value = dep.xpath('@value').extract()
            if (value[0] != "select"):
                myfile.write("---Department---\n")
                deptHtml = dep.extract()
                print deptHtml
                myfile.write(deptHtml + "\n")
                deptOption = driver.find_element_by_xpath("//select[@id='department_selection']/option[@value='" + value[0] + "']")
                deptOption.click()

                time.sleep(1)
                
                selector = self.convertToScrapyObject(driver.page_source)
                courses = selector.select('//select[@id="course_selection"]/option')
                myfile.write("---Courses---\n")
                for course in courses:
                    value2 = course.xpath('@value').extract()
                    if (value2[0] != "select"):
                        courseHtml = course.extract()
                        print courseHtml
                        myfile.write(courseHtml+"\n")

        myfile.close()
        driver.quit()