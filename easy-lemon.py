#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Defined classes

from db.JobQueryService import JobQueryService
from db.JobResultService import JobResultService
from entities.JobQuery import JobQuery
from spiders.IndeedSpider import IndeedSpider
from url.IndeedUrlCreator import IndeedUrlCreator
from utils import FormatUtils


# External lib
from flask import Flask, render_template, request
import json
# import pandas as pd
import os
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

mongo_db_connection = os.environ.get("MONGO_DB_CLIENT_CREDS")


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/job_search", methods=["POST"])
def execute():
    """
    Entry point for easy-lemon.py. This method begins the job search.
    """
    # Core logic that does the actual searching/parsing.

    # Handle empty request:
    if not request.data:
        return None

    # Extract user-provided inputs.
    job_title = request.json['jobTitle']
    job_location = request.json['jobLocation']
    job_experience = request.json['jobExperience']
    job_salary = request.json['jobSalary']

    job_query = build_job_query(job_title, job_location, job_experience, job_salary)

    # Insert into job_query collection.
    job_query_service = JobQueryService(mongo_db_connection)
    job_query_id = job_query_service.insert_job_query(job_query.job_query).inserted_id
    return execute_indeed_query(job_query, str(job_query_id))

    # process.start()  # the script will block here until the crawling is finished


def execute_indeed_query(job_query, job_query_id):
    indeed_url_creator = \
        IndeedUrlCreator(job_query.get_job_title(), job_query.get_job_location(), job_query.get_job_salary())

    # conducting a request of the stated URL above:
    # print("Creating Indeed url: " + indeed_url_creator.generate_url())
    # indeed_page = requests.get(indeed_url_creator.generate_url())

    subprocess.check_output([
        'scrapy',
        'crawl',
        IndeedSpider.name,
        '-a',
        'url=' + indeed_url_creator.generate_url(),
        '-a',
        'num_results=' + '50',
        '-a',
        'job_query_id=' + job_query_id

    ])

    # Return results back to frontend.
    job_results_service = JobResultService(mongo_db_connection)
    job_results = job_results_service.find_job_results_by_query_id(job_query_id)
    result = json.dumps([record for record in job_results])
    job_results_service.delete_job_results_by_query_id(job_query_id)

    return result


def build_job_query(job_title, job_location, job_experience, job_salary=""):
    """
    Builds a JobQuery object. This method will deal with sanitization and lowercasing as well.
    TODO: Sanitization.
    :param job_title: The desired title for the job.
    :param job_location: The desired location for the job.
    :param job_experience: The specified years of experience
    :param job_salary: The desired salary for the job.
    :return: JobQuery
    """
    job_query = {
        'title': job_title.lower(),
        'location': job_location.lower(),
        'experience': job_experience.lower(),
        'salary': job_salary.lower(),
        'keywords': None}
    return JobQuery(job_query)


if __name__ == "__main__":
    # execute()
    app.run(debug=True)

