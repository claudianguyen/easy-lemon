from parse.BaseParser import BaseParser

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from lemon_peeler.lemon_peeler.items import JobInfo


class IndeedParser(BaseParser):
    """ Represents a parser for Indeed. """
    BASE_URL = "https://www.indeed.com/"
    JOB_SECTION_HEADER = "jobSectionHeader"

    def __init__(self, html_page):
        """ Initializes the data."""
        super().__init__(html_page)

    def extract_job_results(self):
        desc_number = 0
        # print(self.html_page)
        # Iterate through all job results for Indeed (on the first page).
        for job_row in self.html_page.find_all(name="div", attrs={"data-tn-component": "organicJob"}):
            # Grab basic info for jobInfo based on the results page.
            job_info = self.setup_job_info(job_row)
            with open("samples/indeed/descriptions/description" + str(desc_number) + ".html", "r") as job_description:
                description_sample = job_description.read()
                description_soup = BeautifulSoup(description_sample, "html.parser")
                should_include_job_info = self.filter_job_description(description_soup)
                job_description.close()
                if should_include_job_info:
                    self.job_results.append(job_info)

        print(len(self.job_results))

    def setup_job_info(self, job_row):
        """
        Returns and sets up the intial jobInfo acquired from the results page.
        :param job_row: a row from the job results page.
        :return: jobInfo
        """
        job_info = JobInfo()
        # Parse company name.
        job_info['job_company'] = job_row.find(name="span", attrs={"class", "company"}).text.strip()
        # Parse listed location from result.
        job_info['job_location'] = job_row.find(name="span", attrs={"class", "location"}).text.strip()
        # Grad the element containing the job title and job url.
        title_and_url = job_row.find(name="a", attrs={"data-tn-element": "jobTitle"})
        # Since Indeed's urls are relative urls, we need to join them with the domain to acquire the absolute url.
        job_info['job_url'] = urljoin(self.BASE_URL, title_and_url.attrs['href'])
        job_info['job_title'] = title_and_url.text.strip()
        snippet = job_row.find(name="td", attrs={"class", "snip"})
        salary_element = snippet.find(name="span", attrs={"class", "no-wrap"})
        job_info['job_salary'] = salary_element.text.strip() if salary_element else "N/A"
        print(job_info)
        return job_info

    def filter_job_description(self, job_description):
        """
        Helper method to parse values and perform filtering for a job description.
        :return: boolean to indicate whether we should filter the result or not.
        """
        criteria = job_description.find_all(name="h3", attrs={"class", self.JOB_SECTION_HEADER})
        if criteria:
            print([criterion.parent for criterion in criteria])
        return True
