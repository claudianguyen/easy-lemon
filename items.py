# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class JobInfo(Item):
    """
    Models for Job Info
    """
    job_title = Field()
    job_location = Field()
    job_url = Field()
    job_company = Field()
    job_salary = Field()
    job_exp = Field()
    pass
