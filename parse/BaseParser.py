import requests
import bs4
from bs4 import BeautifulSoup
from entities.JobInfo import JobInfo

class BaseParser:
    """ Represents a parse. Want to parse each result. """

    def __init__(self, html_page):
        """Initializes the data."""
        self.html_page = html_page
        self.job_results = []

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
        self.job_results = self.job_results.append(JobInfo("Title", "Location", "Company", "URL", "Salary"))
