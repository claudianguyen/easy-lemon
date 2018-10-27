import requests
import bs4
from bs4 import BeautifulSoup
import urllib.parse

from entities.JobInfo import JobInfo

class BaseParser:
    """ Represents a parser. Want to parse each result. """

    def __init__(self, html_page):
        """Initializes the data."""
        self.html_page = html_page
        self.job_results = []
        self.num_filtered_results = 0

    def get_job_results(self):
        """
        Returns the list of JobInfo object created by our parsing logic.
        :return:
        """
        return self.job_results

    def extract_job_results(self):
        """
        Entry point for the parsing of the job information for our job search.
        :return:
        """
        self.job_results.append(JobInfo("Title", "Location", "Company", "URL", "Salary"))

    def get_num_results(self):
        """
        Returns the number of results fetched from the search parameters.
        :return: integer
        """
        return self.num_results

    def get_num_filtered_results(self):
        """
        Returns the number of job results returned after filtering.
        :return: integer
        """
        return self.num_filtered_results

