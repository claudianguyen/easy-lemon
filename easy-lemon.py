#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Defined classes
from entities.JobQuery import JobQuery
from spiders.example import ExampleSpider
from spiders.IndeedSpider import IndeedSpider
from url.IndeedUrlCreator import IndeedUrlCreator
from utils import FormatUtils



# External lib
from flask import Flask, render_template, request
import json
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
        job_results = json.load(items_file)
        return json.dumps(
            sorted(
                [job_result for job_result in job_results],
                key=lambda result: compute_job_result_priority(result, job_query),
                reverse=True))


def compute_job_result_priority(job_result, job_query):
    """
    Computes a "point-value" for the given job_result, which will be used for prioritization of the job_results.
    :param job_result: The job_result to prioritize.
    :param job_query: The job_query that the user provided.
    :return: Point value for this job_result.
    """
    points = 0
    points += compute_salary_points(job_result['job_salary'], job_query) \
              + compute_exp_points(job_result['job_exp'], job_query)
    return points


def compute_exp_points(exp, job_query):
    """
    Computes the "point-value" for the given number of years of experience.
    :param exp: Raw string representing the number of years of experience.
    :param job_query: Job_query provided by the user.
    :return: Point value for the given number of years of experience.
    """
    desired_exp = 2
    if exp == "N/A":
        return 0
    # Years of experience might be a range, so parse out the hyphen.
    years_of_exp = exp.split('-')
    # May contain a '+', so replace that with whitespace.
    exp_low = years_of_exp[0].replace('+', '').strip()
    if len(years_of_exp) > 1:
        exp_high = years_of_exp[1].replace('+', '').strip()
    exp_number = int(exp_low)
    # points = 0.2 - abs(exp_number - desired_exp) / 50
    points = 1 - abs(exp_number - desired_exp) / 50
    return points


def compute_salary_points(salary, job_query):
    """
    Computes the "point-value" for the job_salary portion.
    1: greater than expected
    0.5: No salary information
    0: Below expected.
    :param salary: The salary portion saved by the job_result.
    :param job_query: The job_query provided by the user.
    :return:
    """
    if salary == "N/A" or job_query.get_job_salary() is None:
        return 0.5
    try:
        desired_salary = int(FormatUtils.currency_string_to_basic_string(job_query.get_job_salary()))
        # For now, we bank on the low side of the salary.
        salary_range = salary.split('-')
        if len(salary_range) > 1:
            salary_range[0] = FormatUtils.currency_string_to_basic_string(salary_range[0])
            # Second number represents range, may have additional characters after it. We should remove these.
            salary_range[1].split()
            salary_number_high = int(FormatUtils.currency_string_to_basic_string(salary_range[1][0].strip()))
            salary_number_low = int(salary_range[0])
            return 1 \
                if (salary_number_low and salary_number_low > desired_salary or salary_number_high > desired_salary) \
                else 0

        else:
            salary_number = int(salary_range[0].replace(',', '').strip())
            return 1 if salary_number and salary_number > desired_salary else 0
    except ValueError:
        return 0.5


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

