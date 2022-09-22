import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
from itertools import product
from re import compile
import sys
import re

x = datetime.datetime.now()
t = x.strftime('%c')
ti = str(t)

num_patt = compile('\[([\d,]+)\]')

def parse_url(url):
    urls = []
    ranges = []
    for range_str in num_patt.findall(url):
        # replace this current range string with a digit format placeholder
        url = url.replace('[%s]' % range_str, '%d', 1)
        # make a tuple of the found range
        range_tpl = tuple([int(x) for x in range_str.split(',')])
        # push it in our ranges list
        ranges.append(range_tpl)
    
    # ranges is just a list of tuples at this point so we need to make them ranges
    ranges = [range(*r) for r in ranges]
    
    # create the url permutations
    perms = [p for p in product(*tuple(ranges))]
    for perm in perms:
        urls.append(url % perm)
    
    return urls

class JobSpider(CrawlSpider):
    name = 'i-jobthai'

    def start_requests(self):
        url = 'https://www.i-jobthai.com/index.php?go=view_job&id_job=[1,900]'
        urls = parse_url(url)
        for i in urls:
            yield scrapy.Request(url=i, callback=self.parse_item)

    def parse_item(self, response):

        job_name = response.css('#print2 tr:nth-child(1) td+ td font').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Company name
        company_name = response.css('u b').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"

        # Company location
        company_location = response.css('br~ table+ table tr:nth-child(1) font').getall()
        company_location_str = ''.join(company_location)
        company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        company_location_str = re.sub("<[^>]+>","", company_location_str)
        company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # When it is empty
        if company_location_str == '':
            company_location_str = "-"

        # Requirement
        job_requirement = response.xpath('//*[(@id = "print2")]//tr[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//font').getall()
        job_requirement_str = ''.join(job_requirement)
        job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # When it is empty
        if job_requirement_str == '':
            job_requirement_str = "-"

        # Welfare
        welfare = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 8) and parent::*)]//td').getall()
        welfare_str = ''.join(welfare)
        welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        welfate_str = re.sub("<[^>]+>","", welfate_str)
        welfate_str = re.sub(r"\s\s+"," ", welfate_str)
        # When it is empty
        if welfare_str == '':
            welfare_str = "-"

        # Salary
        salary = response.xpath('//*[(@id = "print2")]//table[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Detail
        job_detail = response.css('br+ table tr:nth-child(2) font').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://i-jobthai.com/",
            'Company_location ':company_location_str,
            'Date_scrapy ' : ti,
            'Requirement ': job_requirement_str,
            'Company_name ': company_str,
            'Welfare ': welfare_str,
            'Job_name ': job_name_str,
            'Detail ': detail_str,
            'Salary ': salary_str,

        }



