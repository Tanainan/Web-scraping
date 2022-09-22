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
    name = 'minor'
    start_urls = [
        "https://storejobs.minorfood.com/?page=1&pageSize=10&rbBrand=TP%2CSW%2CSZ%2CDQ%2CBK%2CCC%2CTE"
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_css='.widthbutton+ .widthbutton'),
            callback='parse_item',follow=True),
        # next button
        Rule(LinkExtractor(restrict_css='.PagedList-skipToNext a'),
            follow=True)
    ]

    def parse_item(self, response):

        job_name = response.xpath('/html/body/div[1]/form/div/div/div/div[1]/div[2]/p').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Work type
        work_type = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "margin-left-10", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-12", " " ))]//p[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]').getall()
        workType_str = ''.join(work_type)
        workType_str = workType_str.replace("\t","").replace("\n","").replace("\r","")
        workType_str = re.sub("<[^>]+>","", workType_str)
        workType_str = re.sub(r"\s\s+"," ", workType_str)
        # When it is empty
        if workType_str == '':
            workType_str = "-"

        # Province
        province = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "margin-left-10", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "col-md-12", " " ))]//p[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]').getall()
        province_str = ''.join(province)
        province_str = province_str.replace("\t","").replace("\n","").replace("\r","")
        province_str = re.sub("<[^>]+>","", province_str)
        province_str = re.sub(r"\s\s+"," ", province_str)
        # When it is empty
        if province_str == '':
            province_str = "-"

       
        # Detail
        job_detail = response.css('.margin-bottom-10 p+ p').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://storejobs.minorfood.com/",
            'Date_scrapy ' : ti,
            'Business type ':workType_str,
            'Province ': province_str,
            'Job_name ': job_name_str,
            'Detail ': detail_str,

        }



