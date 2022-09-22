# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    URL = scrapy.Field()
    Web_name = scrapy.Field()
    Date_scrapy = scrapy.Field()
    Company_name = scrapy.Field()
    Province = scrapy.Field()
    Company_location = scrapy.Field()
    Job_name = scrapy.Field()
    Requirement = scrapy.Field()
    Degree = scrapy.Field()
    Year_experience = scrapy.Field()
    Salary = scrapy.Field()
    Gender = scrapy.Field()
    Welfare = scrapy.Field()
    pass
