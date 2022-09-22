import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import time
import re

x = datetime.datetime.now()
t = x.strftime('%c')
ti = str(t)

class JobSpider(scrapy.Spider):
    name = 'jobnorththailand'

    def start_requests(self):
        driver_path = '/Users/admin/Downloads/chromedriver'
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(driver_path)#, options = options)
        driver.get('https://www.jobnorththailand.com/search')
        time.sleep(2)
        previous_height = driver.execute_script('return document.body.scrollHeight')
        links = []

        while True:
            driver.execute_script('window.scrollTo(0, document.body. scrollHeight);')
            expand_button = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "text-center", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-border-radius", " " ))]')
            expand_button.click()
            time.sleep(2)
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == previous_height:
                break
            previous_height = new_height

        link_elements = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "job-item", " " ))]')

        for link_el in link_elements:
            href = link_el.get_attribute("href")
            yield scrapy.Request(href)


    def parse(self, response):
            
        job_name = response.xpath('/html/body/div[3]/div[5]/div/div[2]/div[2]/div/div[1]/div[1]/h2').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Company name
        # company_name = response.xpath('//b//a').getall()
        # company_str = ''.join(company_name)
        # company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        # company_str = re.sub("<[^>]+>","", company_str)
        # company_str = re.sub(r"\s\s+"," ", company_str)
        # # When it is empty
        # if company_str == '':
        #     company_str = "-"


        # Company location
        # company_location = response.xpath('//font[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        # company_location_str = ''.join(company_location)
        # company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        # company_location_str = re.sub("<[^>]+>","", company_location_str)
        # company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # # When it is empty
        # if company_location_str == '':
        #     company_location_str = "-"
        

        # Requirement
        # job_requirement = response.xpath('//b~//font').getall()
        # job_requirement_str = ''.join(job_requirement)
        # job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        # job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        # job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # # When it is empty
        # if job_requirement_str == '':
        #     job_requirement_str = "-"

        # Detail
        # job_detail = response.xpath('/html/body/div[3]/div/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr/td/table[1]/tbody/tr[3]/td/span/font[2]/text()').getall()
        # detail_str = ''.join(job_detail)
        # detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        # detail_str = re.sub("<[^>]+>","", detail_str)
        # detail_str = re.sub(r"\s\s+"," ", detail_str)
        # # When it is empty
        # if detail_str == '':
        #     detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://www.jobnorththailand.com/",
            'Date_scrapy ' : ti,
            'Job_name ': job_name_str,
            # 'Company_name ': company_str,
            # 'Company_location ':company_location_str,
            # 'Requirement ': job_requirement_str,
            # 'Detail ': detail_str

        }



