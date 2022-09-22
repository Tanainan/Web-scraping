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
    name = 'jobth'
    start_urls = [
        'https://www.jobth.com/searchjob2.php?typejob=&city=&province=&keyword='
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_xpaths='//*[contains(concat( " ", @class, " " ), concat( " ", "w3-round-large", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "w3-padding", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "LinkVisited", " " ))]//b'),
            callback='parse_item',follow=True),
        # next button
        Rule(LinkExtractor(restrict_xpaths='//*[contains(concat( " ", @class, " " ), concat( " ", "paginate", " " )) and (((count(preceding-sibling::*) + 1) = 8) and parent::*)]'),
            follow=True)
    ]

    def parse_item(self, response):

        job_name = response.xpath('/html/body/center/div[3]/center/center/div/div[2]/div/text()').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Work type
        work_type = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "w3-theme-l4", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "w3-medium", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]').getall()
        workType_str = ''.join(work_type)
        workType_str = workType_str.replace("\t","").replace("\n","").replace("\r","")
        workType_str = re.sub("<[^>]+>","", workType_str)
        workType_str = re.sub(r"\s\s+"," ", workType_str)
        # When it is empty
        if workType_str == '':
            workType_str = "-"

        # Company name
        company_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "w3-xlarge", " " )) and contains(concat( " ", @class, " " ), concat( " ", "w3-padding", " " ))]//b').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"

        # Province
        province = response.xpath('/html/body/center/div[3]/center/center/div/div[3]/p[1]/text()').getall()
        province_str = ''.join(province)
        province_str = province_str.replace("\t","").replace("\n","").replace("\r","")
        province_str = re.sub("<[^>]+>","", province_str)
        province_str = re.sub(r"\s\s+"," ", province_str)
        # When it is empty
        if province_str == '':
            province_str = "-"

        # Company location
        company_location = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "w3-xlarge", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "w3-medium", " " ))]').getall()
        company_location_str = ''.join(company_location)
        company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        company_location_str = re.sub("<[^>]+>","", company_location_str)
        company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # When it is empty
        if company_location_str == '':
            company_location_str = "-"

        # People position
        people_position = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "w3-medium", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        people_position_str = ''.join(people_position)
        people_position_str = people_position_str.replace("\t","").replace("\n","").replace("\r","")
        people_position_str = re.sub("<[^>]+>","", people_position_str)
        people_position_str = re.sub(r"\s\s+"," ", people_position_str)
        # When it is empty
        if people_position_str == '':
            people_position_str = "-"


        # Salary
        salary = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "w3-theme-l4", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "w3-medium", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Welfare
        welfare = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "w3-theme-l5", " " ))]//p[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]').getall()
        welfare_str = ''.join(welfare)
        welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        welfare_str = re.sub("<[^>]+>","", welfare_str)
        welfare_str = re.sub(r"\s\s+"," ", welfare_str)
        # When it is empty
        if welfare_str == '':
            welfare_str = "-"

        # Requirement
        job_requirement = response.xpath('//li').getall()
        job_requirement_str = ''.join(job_requirement)
        job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # When it is empty
        if job_requirement_str == '':
            job_requirement_str = "-"

        # Detail
        job_detail = response.xpath('/html/body/center/div[3]/center/center/div/div[6]/p[1]/text()').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://jobth.com/",
            'Date_scrapy ' : ti,
            'Business type ':workType_str,
            'Company_name ': company_str,
            'Province ': province_str,
            'Company_location ':company_location_str,
            'Job_name ': job_name_str,
            'Detail ': detail_str,
            'People_position ': people_position_str,
            'Requirement ': job_requirement_str,
            'Salary ': salary_str,
            'Welfare ': welfare_str,

        }



