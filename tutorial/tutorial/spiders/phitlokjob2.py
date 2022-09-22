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
    name = 'phitlokjob2'

    def start_requests(self):
        url = 'https://www.phitlokjob.com/job_detail/[1,5000]'
        urls = parse_url(url)
        for i in urls:
            yield scrapy.Request(url=i, callback=self.parse_item)

    def parse_item(self, response):

        job_name = response.xpath('//html/body/div/section/div[2]/div/div[2]/h1').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Date release
        date_release = response.xpath('/html/body/div/section/div[2]/div/div[2]/div[3]/text()').getall()
        date_str = ''.join(date_release)
        date_str = date_str.replace("\t","").replace("\n","").replace("\r","")
        date_str = re.sub("<[^>]+>","", date_str)
        date_str = re.sub(r"\s\s+"," ", date_str)
        # When it is empty
        if date_str == '':
            date_str = "-"

        # Work type
        work_type = response.xpath('/html/body/div/section/div[3]/div[1]/div[1]/ul/li[3]/div[2]').getall()
        workType_str = ''.join(work_type)
        workType_str = workType_str.replace("\t","").replace("\n","").replace("\r","")
        workType_str = re.sub("<[^>]+>","", workType_str)
        workType_str = re.sub(r"\s\s+"," ", workType_str)
        # When it is empty
        if workType_str == '':
            workType_str = "-"

        # Company name
        company_name = response.xpath('/html/body/div/section/div[2]/div/div[2]/div[1]/a').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"

        # Province
        province = response.xpath('/html/body/div/section/div[3]/div[1]/div[1]/ul/li[2]/div[2]/a').getall()
        province_str = ''.join(province)
        province_str = province_str.replace("\t","").replace("\n","").replace("\r","")
        province_str = re.sub("<[^>]+>","", province_str)
        province_str = re.sub(r"\s\s+"," ", province_str)
        # When it is empty
        if province_str == '':
            province_str = "-"

        # People position
        people_position = response.xpath('/html/body/div/section/div[3]/div[1]/div[1]/ul/li[4]/div[2]').getall()
        people_position_str = ''.join(people_position)
        people_position_str = people_position_str.replace("\t","").replace("\n","").replace("\r","")
        people_position_str = re.sub("<[^>]+>","", people_position_str)
        people_position_str = re.sub(r"\s\s+"," ", people_position_str)
        # When it is empty
        if people_position_str == '':
            people_position_str = "-"

        # Salary
        salary = response.xpath('/html/body/div/section/div[3]/div[1]/div[1]/ul/li[1]/div[2]/span/text()').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Detail
        job_detail = response.xpath('//p').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://phitlokjob.com/",
            'Date_release ': date_str,
            'Date_scrapy ' : ti,
            'Business type ':workType_str,
            'Company_name ': company_str,
            'Province ': province_str,
            'Job_name ': job_name_str,
            'Detail ': detail_str,
            'People_position ': people_position_str,
            'Salary ': salary_str,

        }



