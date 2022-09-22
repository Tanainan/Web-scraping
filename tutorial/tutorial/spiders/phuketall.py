import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
import re

x = datetime.datetime.now()
t = x.strftime('%c')
ti = str(t)

class JobSpider(CrawlSpider):
    name = 'phuketall'
    start_urls = [
        'https://www.phuketall.com/jobs/alljobs'
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_xpaths='//*[contains(concat( " ", @class, " " ), concat( " ", "col", " " ))]//li//a'),
            callback='parse_item',follow=True),
        # next button
        Rule(LinkExtractor(restrict_xpaths='//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "page-link", " " ))]'),
            follow=True)
    ]

    def parse_item(self, response):
            
        job_name = response.xpath('//h2[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Date release
        date_release = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-3", " " )) and (((count(preceding-sibling::*) + 1) = 17) and parent::*)] | //*[contains(concat( " ", @class, " " ), concat( " ", "col-md-9", " " )) and (((count(preceding-sibling::*) + 1) = 18) and parent::*)]//strong').getall()
        date_str = ''.join(date_release)
        date_str = date_str.replace("\t","").replace("\n","").replace("\r","")
        date_str = re.sub("<[^>]+>","", date_str)
        date_str = re.sub(r"\s\s+"," ", date_str)
        # When it is empty
        if date_str == '':
            date_str = "-"

        # Work type
        work_type = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-9", " " )) and (((count(preceding-sibling::*) + 1) = 8) and parent::*)]').getall()
        workType_str = ''.join(work_type)
        workType_str = workType_str.replace("\t","").replace("\n","").replace("\r","")
        workType_str = re.sub("<[^>]+>","", workType_str)
        workType_str = re.sub(r"\s\s+"," ", workType_str)
        # When it is empty
        if workType_str == '':
            workType_str = "-"

        # Company name
        company_name = response.xpath('//h1').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"

        # Company location
        company_location = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mb-4", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        company_location_str = ''.join(company_location)
        company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        company_location_str = re.sub("<[^>]+>","", company_location_str)
        company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # When it is empty
        if company_location_str == '':
            company_location_str = "-"

        # Degree
        degree = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-9", " " )) and (((count(preceding-sibling::*) + 1) = 6) and parent::*)]//strong | //*[contains(concat( " ", @class, " " ), concat( " ", "col-md-3", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]').getall()
        degree_str = ''.join(degree)
        degree_str = degree_str.replace("\t","").replace("\n","").replace("\r","")
        degree_str = re.sub("<[^>]+>","", degree_str)
        degree_str = re.sub(r"\s\s+"," ", degree_str)
        # When it is empty
        if degree_str == '':
            degree_str = "-"

        # People position
        people_position = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-9", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        people_position_str = ''.join(people_position)
        people_position_str = people_position_str.replace("\t","").replace("\n","").replace("\r","")
        people_position_str = re.sub("<[^>]+>","", people_position_str)
        people_position_str = re.sub(r"\s\s+"," ", people_position_str)
        # When it is empty
        if people_position_str == '':
            people_position_str = "-"


        # Salary
        salary = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-9", " " )) and (((count(preceding-sibling::*) + 1) = 10) and parent::*)]').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Welfare
        welfare = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mb-4", " " )) and (((count(preceding-sibling::*) + 1) = 6) and parent::*)]').getall()
        welfare_str = ''.join(welfare)
        welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        welfare_str = re.sub("<[^>]+>","", welfare_str)
        welfare_str = re.sub(r"\s\s+"," ", welfare_str)
        # When it is empty
        if welfare_str == '':
            welfare_str = "-"

        # Requirement
        job_requirement = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mb-4", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        job_requirement_str = ''.join(job_requirement)
        job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # When it is empty
        if job_requirement_str == '':
            job_requirement_str = "-"

        # Detail
        job_detail = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "pt-3", " " ))]').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://phuketall.com/",
            'Date_release ': date_str,
            'Date_scrapy ' : ti,
            'Business type ':workType_str,
            'Company_name ': company_str,
            'Company_location ':company_location_str,
            'Job_name ': job_name_str,
            'Detail ': detail_str,
            'Requirement ': job_requirement_str,
            'Degree ': degree_str,
            'People_position ': people_position_str,
            'Salary ': salary_str,
            'Welfare ': welfare_str,

        }



