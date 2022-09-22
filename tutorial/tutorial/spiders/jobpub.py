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
    name = 'jobpub'

    def start_requests(self):
        driver_path = '/Users/admin/Downloads/chromedriver'
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(driver_path)#, options = options)
        driver.get('https://www.jobpub.com/searchjob')
        time.sleep(2)
        previous_height = driver.execute_script('return document.body.scrollHeight')
        links = []

        while True:
            driver.execute_script('window.scrollTo(0, document.body. scrollHeight);')
            time.sleep(2)
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == previous_height:
                break
            previous_height = new_height

        link_elements = driver.find_elements_by_xpath('/html/body/div[3]/div/table/tbody/tr[2]/td/table/tbody/tr[6]/td/div/table/tbody/tr[3]/td/div/table/tbody/tr[*]/td/div[2]/p/a[*]')
        link_elements_2 = driver.find_elements_by_xpath('/html/body/div[3]/div/table/tbody/tr[2]/td/table/tbody/tr[6]/td/div/table/tbody/tr[3]/td/div/div[*]/table/tbody/tr[*]/td/div[2]/p/a[*]')

        for link_el in link_elements:
            href = link_el.get_attribute("href")
            yield scrapy.Request(href)

        for link_el_2 in link_elements_2:
            href = link_el_2.get_attribute("href")
            yield scrapy.Request(href)

    def parse(self, response):
            
        job_name = response.xpath('//h1').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)
        
        # Company name
        company_name = response.xpath('//b//a').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"


        # Company location
        company_location = response.xpath('//font[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        company_location_str = ''.join(company_location)
        company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        company_location_str = re.sub("<[^>]+>","", company_location_str)
        company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # When it is empty
        if company_location_str == '':
            company_location_str = "-"
        

        # Detail
        job_detail = response.css('tr:nth-child(3) > td font').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://jobpub.com/",
            'Date_scrapy ' : ti,
            'Job_name ': job_name_str,
            'Company_name ': company_str,
            'Company_location ':company_location_str,
            'Detail ': detail_str

        }



