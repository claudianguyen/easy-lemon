#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Defined classes
from entities.JobQuery import JobQuery
from parse.IndeedParser import IndeedParser
from url.IndeedUrlCreator import IndeedUrlCreator
from url.LinkedInUrlCreator import LinkedInUrlCreator

# Sample generator class
from samples.SampleDataCreator import SampleDataCreator


# External libraries
from bs4 import BeautifulSoup
import requests

# import pandas as pd
# import time


def execute():
    """
    Entry
    """
    # Core logic that does the actual searching/parsing.
    print("Hello World")

    job_query = build_job_query("Software Engineer", "San Francisco", "120,000")
    execute_indeed_query(job_query)
    execute_linkedin_query(job_query)


def execute_indeed_query(job_query):
    """
    Executes job queries for Indeed.
    :param job_query: Desired search parameters
    """
    indeed_url_creator = \
        IndeedUrlCreator(job_query.get_job_title(), job_query.get_job_location(), job_query.get_job_salary())

    # conducting a request of the stated URL above:
    print("Creating Indeed url: " + indeed_url_creator.generate_url())
    # indeed_page = requests.get(indeed_url_creator.generate_url())

    # specifying a desired format of “page” using the html parser - this allows python to read the various components
    # of the page, rather than treating it as one long string.

    indeed_page_sample = ""

    with open("samples/indeed/searchResults.html", "r") as indeed_file:
        indeed_page_sample = indeed_file.read()

    # indeed_soup = BeautifulSoup(indeed_page.text, "html.parser")
    indeed_soup = BeautifulSoup(indeed_page_sample, "html.parser")

    # printing soup in a more structured tree format that makes for easier reading
    # print(indeed_soup.prettify())
    indeed_parser = IndeedParser(indeed_soup)
    indeed_parser.extract_job_results()
    indeed_job_results = indeed_parser.get_job_results()
    print(indeed_job_results)


def create_sample_data(job_results, job_site):
    """
    Creates sample data into samples folder
    :return: void
    """
    sample_data_creator = SampleDataCreator()
    sample_data_creator.create_description_files(job_results, job_site)
    print("Finished creating sample data in samples/indeed/descriptions.")


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


def execute_linkedin_query(job_query):
    """
    Executes job queries for LinkedIn
    :param: job_query: Desired search parameters
    """
    linkedin_url_creator = LinkedInUrlCreator(job_query.get_job_title(), job_query.get_job_location())
    print("Creating LinkedIn url: ", linkedin_url_creator.generate_url())


if __name__ == "__main__":
    execute()




