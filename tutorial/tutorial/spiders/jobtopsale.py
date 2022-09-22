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
    name = 'jobtopsale'

    def start_requests(self):
        url = 'https://jobtopsale.com/jobs/[1,600]?query'
        urls = parse_url(url)
        for i in urls:
            yield scrapy.Request(url=i, callback=self.parse_item)

    def parse_item(self, response):

        job_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "position_text", " " ))]').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Date release
        date_release = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "tag-clock-register", " " ))]//span').getall()
        date_str = ''.join(date_release)
        date_str = date_str.replace("\t","").replace("\n","").replace("\r","")
        date_str = re.sub("<[^>]+>","", date_str)
        date_str = re.sub(r"\s\s+"," ", date_str)
        # When it is empty
        if date_str == '':
            date_str = "-"

        # Work type
        work_type = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "detail_job_bottom_end", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "list_detail_job", " " ))]').getall()
        workType_str = ''.join(work_type)
        workType_str = workType_str.replace("\t","").replace("\n","").replace("\r","")
        workType_str = re.sub("<[^>]+>","", workType_str)
        workType_str = re.sub(r"\s\s+"," ", workType_str)
        # When it is empty
        if workType_str == '':
            workType_str = "-"

        # Company name
        company_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "tag_company_in", " " ))]//a').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"

        # Province
        province = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "position_location_post", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "text_location_job_post", " " ))]').getall()
        province_str = ''.join(province)
        province_str = province_str.replace("\t","").replace("\n","").replace("\r","")
        province_str = re.sub("<[^>]+>","", province_str)
        province_str = re.sub(r"\s\s+"," ", province_str)
        # When it is empty
        if province_str == '':
            province_str = "-"

        # People position
        people_position = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "tag-employee-register", " " ))]//span').getall()
        people_position_str = ''.join(people_position)
        people_position_str = people_position_str.replace("\t","").replace("\n","").replace("\r","")
        people_position_str = re.sub("<[^>]+>","", people_position_str)
        people_position_str = re.sub(r"\s\s+"," ", people_position_str)
        # When it is empty
        if people_position_str == '':
            people_position_str = "-"

        # Salary
        salary = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "tag-money", " " ))]//span').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Welfare
        welfare = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "other-benifit", " " )) and contains(concat( " ", @class, " " ), concat( " ", "detail_job_bottom", " " ))]').getall()
        welfare_str = ''.join(welfare)
        welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        welfare_str = re.sub("<[^>]+>","", welfare_str)
        welfare_str = re.sub(r"\s\s+"," ", welfare_str)
        # When it is empty
        if welfare_str == '':
            welfare_str = "-"

        # Requirement
        job_requirement = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-12", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "col-12", " " ))]').getall()        
        job_requirement_str = ''.join(job_requirement)
        job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # When it is empty
        if job_requirement_str == '':
            job_requirement_str = "-"

        # Detail
        job_detail = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "detail_job", " " ))]').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://jobtopsale.com/",
            'Date_release ': date_str,
            'Date_scrapy ' : ti,
            'Business type ':workType_str,
            'Company_name ': company_str,
            'Province ': province_str,
            'Job_name ': job_name_str,
            'Detail ': detail_str,
            'Requirement ': job_requirement_str,
            'People_position ': people_position_str,
            'Salary ': salary_str,
            'Welfare ': welfare_str,

        }



