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
    name = 'Job2'
    start_urls = [
        "https://thaijobtoday.com/"
    ]

    # Set up rule for linking another page
    rules = [
        # inside card
        Rule(LinkExtractor(restrict_xpaths='//*[(@id = "recent_job_div")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-block", " " ))]'),
            callback='parse_item',follow=True),
        # next button
        Rule(LinkExtractor(restrict_xpaths='//*[(@id = "recent_job_div")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-warning", " " ))]'),
            follow=True)
    ]

    def parse_item(self, response):
            
        job_name = response.xpath('//h3/text()').getall()
        job_name_str = ''.join(job_name)
        job_name_str = job_name_str.replace("\t","").replace("\n","").replace("\r","")
        job_name_str = re.sub("<[^>]+>","", job_name_str)
        job_name_str = re.sub(r"\s\s+"," ", job_name_str)

        # Detail
        job_detail = response.xpath('//td').getall()
        detail_str = ''.join(job_detail)
        detail_str = detail_str.replace("\t","").replace("\n","").replace("\r","")
        detail_str = re.sub("<[^>]+>","", detail_str)
        detail_str = re.sub(r"\s\s+"," ", detail_str)
        # When it is empty
        if detail_str == '':
            detail_str = "-"

        yield {
            'URL ': response.url,
            'Web name ': "https://thaijobtoday.com/",
            'Date_scrapy ' : ti,
            'Job_name ': job_name_str,
            'Detail ': detail_str,

        }



