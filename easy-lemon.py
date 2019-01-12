#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Defined classes
from entities.JobQuery import JobQuery
from spiders.example import ExampleSpider
from spiders.IndeedSpider import IndeedSpider
from url.IndeedUrlCreator import IndeedUrlCreator


# External lib
from flask import Flask, render_template, request
# import pandas as pd
# import time
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
import subprocess


app = Flask(__name__)

# Crawler process for scraping.
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

crawler_settings = {'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/job_search", methods=["POST"])
def execute():
    """
    Entry point for easy-lemon.py. This method begins the job search.
    """
    # Core logic that does the actual searching/parsing.

    # Extract user-provided inputs.
    job_title = request.json['jobTitle']
    job_location = request.json['jobLocation']
    job_salary = request.json['jobSalary']

    job_query = build_job_query(job_title, job_location, job_salary)
    return execute_indeed_query(job_query)

    # process.start()  # the script will block here until the crawling is finished


def execute_indeed_query(job_query):
    indeed_url_creator = \
        IndeedUrlCreator(job_query.get_job_title(), job_query.get_job_location(), job_query.get_job_salary())

    # conducting a request of the stated URL above:
    # print("Creating Indeed url: " + indeed_url_creator.generate_url())
    # indeed_page = requests.get(indeed_url_creator.generate_url())
    # Clear output.json file.
    open("output.json", 'w').close()

    subprocess.check_output([
        'scrapy',
        'crawl',
        IndeedSpider.name,
        '-a',
        'url=' + indeed_url_creator.generate_url(),
        '-a',
        'num_results=' + '50',
        '-o',
        'output.json'
    ])

    # Return results back to frontend.
    with open("output.json") as items_file:
        return items_file.read()


def build_job_query(job_title, job_location, job_salary=""):
    """
    Builds a JobQuery object. This method will deal with sanitization and lowercasing as well.
    TODO: Sanitization.
    :param job_title: The desired title for the job.
    :param job_location: The desired location for the job.
    :param job_salary: The desired salary for the job.
    :return: JobQuery
    """
    return JobQuery(job_title.lower(), job_location.lower(), job_salary.lower())


if __name__ == "__main__":
    # execute()
    app.run(debug=True)

