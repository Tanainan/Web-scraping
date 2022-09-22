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
    name = 'jobmobi'
    start_urls = [
        "https://www.jobmobi.com/joblistbytype.php"
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_xpaths='/html/body/div/section/div[2]/div[2]/div[1]/div[*]/div/div[2]/div[1]/a[1]'),
            callback='parse_item',follow=True),
        # next button
        Rule(LinkExtractor(restrict_xpaths='/html/body/div/section/div[2]/div[2]/div[2]/nav/ul/li[17]/a'),
            follow=True)
    ]

    def parse_item(self, response):

        job_name = response.xpath('/html/body/div[1]/section/div[1]/div/font/b/a[4]').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Company name
        # company_name = response.xpath('//h3/text()').getall()
        # company_str = ''.join(company_name)
        # company_str = company_str.replace("\t","").replace("\n","").replace("\r","")
        # company_str = re.sub("<[^>]+>","", company_str)
        # company_str = re.sub(r"\s\s+"," ", company_str)
        # # When it is empty
        # if company_str == '':
        #     company_str = "-"

        # Province
        # province = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 9) and parent::*)]//td').getall()
        # province_str = ''.join(province)
        # province_str = province_str.replace("\t","").replace("\n","").replace("\r","")
        # province_str = re.sub("<[^>]+>","", province_str)
        # province_str = re.sub(r"\s\s+"," ", province_str)
        # # When it is empty
        # if province_str == '':
        #     province_str = "-"

        # Company location
        # company_location = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 8) and parent::*)]//td').getall()
        # company_location_str = ''.join(company_location)
        # company_location_str = company_location_str.replace("\t","").replace("\n","").replace("\r","")
        # company_location_str = re.sub("<[^>]+>","", company_location_str)
        # company_location_str = re.sub(r"\s\s+"," ", company_location_str)
        # # When it is empty
        # if company_location_str == '':
        #     company_location_str = "-"

        # Degree
        # degree = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//td').getall()
        # degree_str = ''.join(degree)
        # degree_str = degree_str.replace("\t","").replace("\n","").replace("\r","")
        # degree_str = re.sub("<[^>]+>","", degree_str)
        # degree_str = re.sub(r"\s\s+"," ", degree_str)

        # Year experience
        # year_experience = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//td').getall()
        # year_experience_str = ''.join(year_experience)
        # year_experience_str = year_experience_str.replace("\t","").replace("\n","").replace("\r","")
        # year_experience_str = re.sub("<[^>]+>","", year_experience_str)
        # year_experience_str = re.sub(r"\s\s+"," ", year_experience_str)
        # # When it is empty
        # if year_experience_str == '':
        #     year_experience_str = "-"


        # Gender
        # gender = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//td').getall()
        # gender_str = ''.join(gender)
        # gender_str = gender_str.replace("\t","").replace("\n","").replace("\r","")
        # gender_str = re.sub("<[^>]+>","", gender_str)
        # gender_str = re.sub(r"\s\s+"," ", gender_str)
        # # When it is empty
        # if gender_str == '':
        #     gender_str = "-"

        # Salary
        # salary = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//td').getall()
        # salary_str = ''.join(salary)
        # salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        # salary_str = re.sub("<[^>]+>","", salary_str)
        # salary_str = re.sub(r"\s\s+"," ", salary_str)
        # # When it is empty
        # if salary_str == '':
        #     salary_str = "-"

        # Welfare
        # welfare = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 7) and parent::*)]//td').getall()
        # welfare_str = ''.join(welfare)
        # welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        # welfare_str = re.sub("<[^>]+>","", welfare_str)
        # welfare_str = re.sub(r"\s\s+"," ", welfare_str)
        # # When it is empty
        # if welfare_str == '':
        #     welfare_str = "-"

        # Requirement
        # job_requirement = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]//td').getall()
        # job_requirement_str = ''.join(job_requirement)
        # job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        # job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        # job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # # When it is empty
        # if job_requirement_str == '':
        #     job_requirement_str = "-"

        # Detail
        # job_detail = response.xpath('//tr[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//td').getall()
        # detail_str = ''.join(job_detail)
        # detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        # detail_str = re.sub("<[^>]+>","", detail_str)
        # detail_str = re.sub(r"\s\s+"," ", detail_str)
        # # When it is empty
        # if detail_str == '':
        #     detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://jobmobi.com/",
            'Date_scrapy ' : ti,
            # 'Company_name ': company_str,
            # 'Province ': province_str,
            # 'Company_location ':company_location_str,
            'Job_name ': job_name_str,
            # 'Requirement ': job_requirement_str,
            # 'Degree ': degree_str,
            # 'Year_experience ': year_experience_str,
            # 'Salary ': salary_str,
            # 'Gender ': gender_str,
            # 'Welfare ': welfare_str,

        }



