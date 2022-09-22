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
    name = 'jobkia'
    start_urls = [
        "https://www.jobkia.com/jobs?typejobs=&typebusiness=&worklocation=&amphures=&districts=&educationlevel=&salary=&termemployment=&industry=&qs=&post=post"
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_xpaths='/html/body/div[2]/div/div/section[3]/div/div/div[*]/div[2]/a'),
            callback='parse_item',follow=True)
    ]
    def parse_item(self, response):

        job_name = response.xpath('/html/body/div[2]/div/div[1]/div[5]/div[1]/ul/li[1]/span').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Company name
        company_name = response.xpath('/html/body/div[2]/div/div[1]/div[3]/div/h3').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"


        # Company location
        company_location = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "job-bottom", " " ))]//hr+//*[contains(concat( " ", @class, " " ), concat( " ", "margin-bottom", " " ))]').getall()
        company_location_str = ''.join(company_location)
        company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        company_location_str = re.sub("<[^>]+>","", company_location_str)
        company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # When it is empty
        if company_location_str == '':
            company_location_str = "-"

        # Degree
        degree = response.xpath('//p[(((count(preceding-sibling::*) + 1) = 10) and parent::*)]').getall()
        degree_str = ''.join(degree)
        degree_str = degree_str.replace("\t","").replace("\n","").replace("\r","")
        degree_str = re.sub("<[^>]+>","", degree_str)
        degree_str = re.sub(r"\s\s+"," ", degree_str)

        # Salary
        salary = response.xpath('/html/body/div[2]/div/div[1]/div[6]/div[2]').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Welfare
        welfare = response.xpath('//p[(((count(preceding-sibling::*) + 1) = 14) and parent::*)]').getall()
        welfare_str = ''.join(welfare)
        welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        welfare_str = re.sub("<[^>]+>","", welfare_str)
        welfare_str = re.sub(r"\s\s+"," ", welfare_str)
        # When it is empty
        if welfare_str == '':
            welfare_str = "-"

        # Requirement
        job_requirement = response.xpath('/html/body/div[2]/div/div[1]/div[5]/div[2]/p[2]').getall()
        job_requirement_str = ''.join(job_requirement)
        job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # When it is empty
        if job_requirement_str == '':
            job_requirement_str = "-"

        # Detail
        job_detail = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "job-bottom", " " ))]//p[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        # People position
        people_position = response.xpath('/html/body/div[2]/div/div[1]/div[6]/div[2]').getall()
        people_position_str = ''.join(people_position)
        people_position_str = people_position_str.replace("\t","").replace("\n","").replace("\r","").replace(r"<[^>]+>","")
        people_position_str = re.sub("<[^>]+>","", people_position_str)
        people_position_str = re.sub(r"\s\s+"," ", people_position_str)
        # When it is empty
        if people_position_str == '':
            people_position_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://jobkia.com/",
            'Date_scrapy ' : ti,
            'Company_name ': company_str,
            'Company_location ':company_location_str,
            'Job_name ': job_name_str,
            'Requirement ': job_requirement_str,
            'Detail ': detail_str,
            'Degree ': degree_str,
            'People_position ': people_position_str,
            'Salary ': salary_str,
            'Welfare ': welfare_str,

        }



