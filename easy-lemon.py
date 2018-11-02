#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Defined classes
from entities.JobQuery import JobQuery
from lemon_peeler.lemon_peeler.spiders.IndeedSpider import IndeedSpider
from parse.IndeedParser import IndeedParser
from samples.SampleDataCreator import SampleDataCreator
from url.IndeedUrlCreator import IndeedUrlCreator


# External libraries
from bs4 import BeautifulSoup
import requests

# import pandas as pd
# import time
import scrapy
from scrapy.crawler import CrawlerProcess


# Crawler process for scraping.
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

def execute():
    """
    Entry point for easy-lemon.py. This method begins the job search.
    """
    # Core logic that does the actual searching/parsing.
    print("Hello World")
    print("Creating url...")

    job_query = build_job_query("Software Engineer", "San Francisco", "120,000")
    execute_indeed_query(job_query)

    process.start()  # the script will block here until the crawling is finished


def execute_indeed_query(job_query):
    indeed_url_creator = \
        IndeedUrlCreator(job_query.get_job_title(), job_query.get_job_location(), job_query.get_job_salary())

    # conducting a request of the stated URL above:
    print("Creating Indeed url: " + indeed_url_creator.generate_url())
    # indeed_page = requests.get(indeed_url_creator.generate_url())

    # specifying a desired format of “page” using the html parser - this allows python to read the various components
    # of the page, rather than treating it as one long string.

    indeed_page_sample = ""
    process.crawl(IndeedSpider, indeed_url_creator.generate_url())

    with open("samples/indeed/searchResults.html", "r") as indeed_file:
        indeed_page_sample = indeed_file.read()

    # indeed_soup = BeautifulSoup(indeed_page.text, "html.parser")
    indeed_soup = BeautifulSoup(indeed_page_sample, "html.parser")

    # printing soup in a more structured tree format that makes for easier reading
    # print(indeed_soup.prettify())
    indeed_parser = IndeedParser(indeed_soup)
    # indeed_parser.extract_job_results()
    # indeed_job_results = indeed_parser.get_job_results()
    # print(indeed_job_results)

    # Create sample descriptions (for indeed)
    # sample_data_creator = SampleDataCreator()
    # sample_data_creator.create_description_files(indeed_job_results, "indeed")
    # print("Finished creating sample data in samples/indeed/descriptions.")


def build_job_query(job_title, job_location, job_salary=""):
    """
    Builds a JobQuery object. This method will deal with sanitization and lowercaseing as well.
    TODO: Sanitization.
    :param job_title: The desired title for the job.
    :param job_location: The desired location for the job.
    :param job_salary: The desired salary for the job.
    :return: JobQuery
    """
    return JobQuery(job_title.lower(), job_location.lower(), job_salary.lower())


if __name__ == "__main__":
    execute()
