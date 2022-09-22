import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
import re

x = datetime.datetime.now()
t = x.strftime('%c')
ti = str(t)

class JobSpider(scrapy.Spider):
    name = 'techstar'

    def start_requests(self):
        driver_path = '/Users/admin/Downloads/chromedriver'
        options = ChromeOptions()
        options.headless = True
        driver = Chrome(driver_path, options = options)
        driver.get('https://www.techstarthailand.com/jobSearch?keywords=')
        link_elements = driver.find_elements_by_xpath('/html/body/div[1]/div/form/div[2]/div[2]/div/div[2]/div[1]/div[*]/a')

        for link_el in link_elements:
            href = link_el.get_attribute("href")
            yield scrapy.Request(href)

        driver.quit()

    def parse(self, response):
            
        job_name = response.xpath('/html/body/div[1]/div/div[1]/h1/span').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Detail1
        detail1 = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]').getall()
        detail1_str = ''.join(detail1)
        detail1_str = detail1_str.replace("\t","").replace("\n","").replace("\r","")
        detail1_str = re.sub("<[^>]+>","", detail1_str)
        detail1_str = re.sub(r"\s\s+"," ", detail1_str)
        # When it is empty
        if detail1_str == '':
            detail1_str = "-"


        # Detail
        job_detail = response.xpath('/html/body/div[1]/div/div[2]/div[2]').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://techstarthailand.com/",
            'Date_scrapy ' : ti,
            'Job_name ': job_name_str,
            'Detail1 ': detail1_str,
            'Detail ': detail_str

        }



