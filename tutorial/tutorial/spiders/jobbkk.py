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
    name = 'jobbkk'
    start_urls = [
        "https://www.jobbkk.com/%E0%B8%AB%E0%B8%B2%E0%B8%87%E0%B8%B2%E0%B8%99"
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_xpaths='/html/body/section[7]/article/section/div[1]/div[*]/div/div[2]/div[2]/div/div[1]/a'),
            callback='parse_item',follow=True),
        # next button
        Rule(LinkExtractor(restrict_xpaths='/html/body/section[7]/article/section/div[1]/article/div/nav/ul/li[*]/a'),
            follow=True)
    ]

    def parse_item(self, response):
            
        job_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-xs-6", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "text-red", " " ))]').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Company name
        company_name = response.xpath('//h4//a').getall()
        company_str = ''.join(company_name)
        company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        company_str = re.sub("<[^>]+>","", company_str)
        company_str = re.sub(r"\s\s+"," ", company_str)
        # When it is empty
        if company_str == '':
            company_str = "-"

        # Province
        province = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-12", " " )) and contains(concat( " ", @class, " " ), concat( " ", "margin-bottom", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        province_str = ''.join(province)
        province_str = province_str.replace("\t","").replace("\n","").replace("\r","")
        province_str = re.sub("<[^>]+>","", province_str)
        province_str = re.sub(r"\s\s+"," ", province_str)
        # When it is empty
        if province_str == '':
            province_str = "-"

        # Company location
        company_location = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "contact-address", " " ))]//h6').getall()
        company_location_str = ''.join(company_location)
        company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        company_location_str = re.sub("<[^>]+>","", company_location_str)
        company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # When it is empty
        if company_location_str == '':
            company_location_str = "-"

        # Degree
        degree = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "margin-bottom", " " )) and (((count(preceding-sibling::*) + 1) = 8) and parent::*)]//h6[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        degree_str = ''.join(degree)
        degree_str = degree_str.replace("\t","").replace("\n","").replace("\r","")
        degree_str = re.sub("<[^>]+>","", degree_str)
        degree_str = re.sub(r"\s\s+"," ", degree_str)

        # Year experience
        year_experience = response.css('.margin-bottom~ .margin-bottom h6:nth-child(5)').getall()
        year_experience_str = ''.join(year_experience)
        year_experience_str = year_experience_str.replace("\t","").replace("\n","").replace("\r","")
        year_experience_str = re.sub("<[^>]+>","", year_experience_str)
        year_experience_str = re.sub(r"\s\s+"," ", year_experience_str)
        # When it is empty
        if year_experience_str == '':
            year_experience_str = "-"

        # Work type
        work_type = response.css('.margin-bottom:nth-child(4) .margin-bottom-1+ h6').getall()
        workType_str = ''.join(work_type)
        workType_str = workType_str.replace("\t","").replace("\n","").replace("\r","").replace(r"<[^>]+>","")
        workType_str = re.sub("<[^>]+>","", workType_str)
        workType_str = re.sub(r"\s\s+"," ", workType_str)
        # When it is empty
        if workType_str == '':
            workType_str = "-"

        # People position
        people_position = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-12", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//h6[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]').getall()
        people_position_str = ''.join(people_position)
        people_position_str = people_position_str.replace("\t","").replace("\n","").replace("\r","").replace(r"<[^>]+>","")
        people_position_str = re.sub("<[^>]+>","", people_position_str)
        people_position_str = re.sub(r"\s\s+"," ", people_position_str)
        # When it is empty
        if people_position_str == '':
            people_position_str = "-"

        # Gender
        gender = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "margin-bottom", " " )) and (((count(preceding-sibling::*) + 1) = 8) and parent::*)]//h6[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]').getall()
        gender_str = ''.join(gender)
        gender_str = gender_str.replace("\t","").replace("\n","").replace("\r","")
        gender_str = re.sub("<[^>]+>","", gender_str)
        gender_str = re.sub(r"\s\s+"," ", gender_str)
        # When it is empty
        if gender_str == '':
            gender_str = "-"

        # Age
        age = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "margin-bottom", " " )) and (((count(preceding-sibling::*) + 1) = 8) and parent::*)]//h6[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]').getall()
        age_str = ''.join(age)
        age_str = age_str.replace("\t","").replace("\n","").replace("\r","")
        age_str = re.sub("<[^>]+>","", age_str)
        age_str = re.sub(r"\s\s+"," ", age_str)
        # When it is empty
        if age_str == '':
            age_str = "-"

        # Salary
        salary = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-sm-8", " " ))]//h6[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Welfare
        welfare = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "margin-bottom", " " )) and (((count(preceding-sibling::*) + 1) = 10) and parent::*)]').getall()
        welfare_str = ''.join(welfare)
        welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        welfare_str = re.sub("<[^>]+>","", welfare_str)
        welfare_str = re.sub(r"\s\s+"," ", welfare_str)
        # When it is empty
        if welfare_str == '':
            welfare_str = "-"

        # Requirement
        job_requirement = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "margin-bottom", " " )) and (((count(preceding-sibling::*) + 1) = 8) and parent::*)]').getall()
        job_requirement_str = ''.join(job_requirement)
        job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # When it is empty
        if job_requirement_str == '':
            job_requirement_str = "-"

        # Detail
        job_detail = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-12", " " )) and contains(concat( " ", @class, " " ), concat( " ", "margin-bottom", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://jobbkk.com/",
            'Date_scrapy ' : ti,
            'Business type ':workType_str,
            'Company_name ': company_str,
            'Province ': province_str,
            'Company_location ':company_location_str,
            'Job_name ': job_name_str,
            'Requirement ': job_requirement_str,
            'Degree ': degree_str,
            'Year_experience ': year_experience_str,
            'Salary ': salary_str,
            'Gender ': gender_str,
            'People_position ': people_position_str,
            'Age ': age_str,
            'Welfare ': welfare_str,

        }



