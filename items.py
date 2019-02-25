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
    jobTitle = Field()
    jobLocation = Field()
    jobUrl = Field()
    jobCompany = Field()
    jobSalary = Field()
    jobExp = Field()
    jobPoints = Field()
    pass
