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
    name = 'chiangraifocus'
    def start_requests(self):
        url = 'https://www.chiangraifocus.com/jobs/jobsdetails.php?id=[1,1900]'
        urls = parse_url(url)
        for i in urls:
            yield scrapy.Request(url=i, callback=self.parse_item)


    def parse_item(self, response):
            
        job_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "d-flex", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "p-2", " " ))]').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Company name
        company_name = response.xpath('/html/body/div[2]/article/div[2]/div[2]/div/div/div/div[2]/div[1]/div[4]/div/text()').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"


        # Company location
        company_location = response.xpath('/html/body/div[2]/article/div[2]/div[2]/div/div/div/div[2]/div[1]/div[5]/div/text()').getall()
        company_location_str = ''.join(company_location)
        company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        company_location_str = re.sub("<[^>]+>","", company_location_str)
        company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # When it is empty
        if company_location_str == '':
            company_location_str = "-"

        # Detail
        job_detail = response.xpath('/html/body/div[2]/article/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/text()').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://chiangraifocus.com/",
            'Date_scrapy ' : ti,
            'Job_name ': job_name_str,
            'Company_name ': company_str,
            'Company_location ':company_location_str,
            'Detail ': detail_str,

        }



