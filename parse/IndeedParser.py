from entities.JobInfo import JobInfo
from parse.BaseParser import BaseParser

from urllib.parse import urljoin


class IndeedParser(BaseParser):
    """ Represents a parser for Indeed. """
    BASE_URL = "https://www.indeed.com/"


    def _init__(self, html_page):
        """ Initializes the data."""
        super()._init__(html_page)

    def extract_job_results(self):
        test_description = 0
        # print(self.html_page)
        # Iterate through all job results for Indeed (on the first page).
        for job_row in self.html_page.find_all(name="div", attrs={"data-tn-component": "organicJob"}):
            # Grab basic info for jobInfo based on the results page.
            self.setup_job_info(job_row)
            with open("samples/indeed/descriptions/description" + str(test_description) + ".html", "r") as job_description:
                description_sample = job_description.read()
                self.filter_job_description(description_sample)
                job_description.close()

        print(len(self.job_results))

    def setup_job_info(self, job_row):
        # Parse company name.
        company = job_row.find(name="span", attrs={"class", "company"}).text.strip()
        # Parse listed location from result.
        location = job_row.find(name="span", attrs={"class", "location"}).text.strip()
        # Grad the element containing the job title and job url.
        title_and_url = job_row.find(name="a", attrs={"data-tn-element": "jobTitle"})
        # Since Indeed's urls are relative urls, we need to join them with the domain to acquire the absolute url.
        url = urljoin(self.BASE_URL, title_and_url.attrs['href'])
        title = title_and_url.text.strip()
        snippet = job_row.find(name="td", attrs={"class", "snip"})
        salary_element = snippet.find(name="span", attrs={"class", "no-wrap"})
        salary = salary_element.text.strip() if salary_element else "N/A"
        job_info = JobInfo(title, location, url, company, salary)
        self.job_results.append(job_info)
        print(job_info)

    def filter_job_description(self, job_description):
        """
        Helper method to parse values and perform filtering for a job description.
        :return: boolean to indicate whether we should filter the result or not.
        """
        print(job_description)
