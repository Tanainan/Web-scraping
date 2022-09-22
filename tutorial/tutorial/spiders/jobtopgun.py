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
    name = 'jobtopgun'
    start_urls = [
        "https://www.jobtopgun.com/search?&source="
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_xpaths='/html/body/div[1]/div[2]/div[2]/div[4]/div[1]/div[.]/div/div[2]/div[2]/div/div[1]/a'),
            callback='parse_item',follow=True),
        # next button
        Rule(LinkExtractor(restrict_xpaths='//*[(@id = "__next")]'),
            follow=True)
    ]

    def parse_item(self, response):

        job_name = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/h1').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Work type
        work_type = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "job-detail-desc1", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "col-5", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "col", " " ))]').getall()
        workType_str = ''.join(work_type)
        workType_str = workType_str.replace("\t","").replace("\n","").replace("\r","")
        workType_str = re.sub("<[^>]+>","", workType_str)
        workType_str = re.sub(r"\s\s+"," ", workType_str)
        # When it is empty
        if workType_str == '':
            workType_str = "-"

        # Company name
        company_name = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"

        # Province
        province = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[2]/div[4]/div[1]/div/div[2]').getall()
        province_str = ''.join(province)
        province_str = province_str.replace("\t","").replace("\n","").replace("\r","")
        province_str = re.sub("<[^>]+>","", province_str)
        province_str = re.sub(r"\s\s+"," ", province_str)
        # When it is empty
        if province_str == '':
            province_str = "-"

        # Company location
        company_location = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[2]/div[13]/div[2]/div[1]/div[2]').getall()
        company_location_str = ''.join(company_location)
        company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        company_location_str = re.sub("<[^>]+>","", company_location_str)
        company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # When it is empty
        if company_location_str == '':
            company_location_str = "-"

        # Degree
        degree = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[2]/div[4]/div[2]/div/div[2]').getall()
        degree_str = ''.join(degree)
        degree_str = degree_str.replace("\t","").replace("\n","").replace("\r","")
        degree_str = re.sub("<[^>]+>","", degree_str)
        degree_str = re.sub(r"\s\s+"," ", degree_str)
        # When it is empty
        if degree_str == '':
            degree_str = "-"

        # Year experience
        year_experience = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]').getall()
        year_experience_str = ''.join(year_experience)
        year_experience_str = year_experience_str.replace("\t","").replace("\n","").replace("\r","")
        year_experience_str = re.sub("<[^>]+>","", year_experience_str)
        year_experience_str = re.sub(r"\s\s+"," ", year_experience_str)
        # When it is empty
        if year_experience_str == '':
            year_experience_str = "-"

        # Salary
        salary = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[2]/div[5]/div/div/div[2]').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Welfare
        welfare = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[2]/div[12]').getall()
        welfare_str = ''.join(welfare)
        welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        welfare_str = re.sub("<[^>]+>","", welfare_str)
        welfare_str = re.sub(r"\s\s+"," ", welfare_str)
        # When it is empty
        if welfare_str == '':
            welfare_str = "-"

        # Requirement
        job_requirement = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "job-detail-desc1", " " )) and (((count(preceding-sibling::*) + 1) = 12) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "jtg-list-bullet", " " ))]').getall()
        job_requirement_str = ''.join(job_requirement)
        job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # When it is empty
        if job_requirement_str == '':
            job_requirement_str = "-"

        # Detail
        job_detail = response.xpath('/html/body/div[1]/section[2]/div[1]/div/div[2]/div[2]/div[8]/div/div').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://jobtopgun.com/",
            'Date_scrapy ' : ti,
            'Business type ':workType_str,
            'Company_name ': company_str,
            'Province ': province_str,
            'Company_location ':company_location_str,
            'Job_name ': job_name_str,
            'Detail ': detail_str,
            'Requirement ': job_requirement_str,
            'Degree ': degree_str,
            'Year_experience ': year_experience_str,
            'Salary ': salary_str,
            'Welfare ': welfare_str,

        }



