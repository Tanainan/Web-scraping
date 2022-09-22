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
    name = 'reeracoen'
    start_urls = [
        "https://www.reeracoen.co.th/th/jobs?s%5Bkeyword%5D=&s%5Bjob_category%5D=&s%5Bworking_location%5D=10726-10727-10728-10729-10730-10731-10732-10733-10734-10735-10736-10737-10738-10739-10740-10741-10742-10743-10744-10745-10746-10747-10748-10749-10750-10751-10752-10753-10754-10755-10756-10757-10758-10759-10760-10761-10762-10763-10764-10765-10766-10767-10768-10769-10770-10771-10772-10773-10774-10775-10776-10777-10778-10967-10968-10969-10970-10971-11027-11028-11029-11030-11031-11032-11033-11034-11035-11036-11037-11038-11039-11040-11041-11042-11043-11044-11045-11046-11047-11048-11049-11050-11051-11052-11053-11054-11055-11056-11057-11065&s%5Bmin_salary%5D=&s%5Bmax_salary%5D=&s%5Bexperience%5D=&s%5Bindustry%5D=&button="
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_xpaths='//*[(@id = "jobs")]//*[contains(concat( " ", @class, " " ), concat( " ", "list", " " ))]//a'),
            callback='parse_item',follow=True),
        # next button
        Rule(LinkExtractor(restrict_xpaths='//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]//a'),
            follow=True)
    ]

    def parse_item(self, response):
            
        job_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "main", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "position", " " ))]').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Province
        province = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "main", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "location", " " ))]').getall()
        province_str = ''.join(province)
        province_str = province_str.replace("\t","").replace("\n","").replace("\r","")
        province_str = re.sub("<[^>]+>","", province_str)
        province_str = re.sub(r"\s\s+"," ", province_str)
        # When it is empty
        if province_str == '':
            province_str = "-"


        # Salary
        salary = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "main", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "salary", " " ))]').getall()
        salary_str = ''.join(salary)
        salary_str = salary_str.replace("\t","").replace("\n","").replace("\r","")
        salary_str = re.sub("<[^>]+>","", salary_str)
        salary_str = re.sub(r"\s\s+"," ", salary_str)
        # When it is empty
        if salary_str == '':
            salary_str = "-"

        # Welfare
        welfare = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "detail", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "list", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "benefit", " " ))]//p').getall()
        welfare_str = ''.join(welfare)
        welfare_str = welfare_str.replace("\t","").replace("\n","").replace("\r","")
        welfare_str = re.sub("<[^>]+>","", welfare_str)
        welfare_str = re.sub(r"\s\s+"," ", welfare_str)
        # When it is empty
        if welfare_str == '':
            welfare_str = "-"

        # Requirement
        job_requirement = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "requirement", " " ))]//p').getall()
        job_requirement_str = ''.join(job_requirement)
        job_requirement_str = job_requirement_str.replace("\t","").replace("\n","").replace("\r","")
        job_requirement_str = re.sub("<[^>]+>","", job_requirement_str)
        job_requirement_str = re.sub(r"\s\s+"," ", job_requirement_str)
        # When it is empty
        if job_requirement_str == '':
            job_requirement_str = "-"

        # Detail
        job_detail = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "detail", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "list", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "description", " " ))]//p').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "ttps://www.reeracoen.co.th",
            'Date_scrapy ' : ti,
            'Province ': province_str,
            'Job_name ': job_name_str,
            'Requirement ': job_requirement_str,
            'Salary ': salary_str,
            'Detail ': detail_str,
            'Welfare ': welfare_str,

        }



