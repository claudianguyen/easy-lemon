
from parse.BaseParser import BaseParser


class IndeedParser(BaseParser):
    """ Represents a parser for Indeed. """
    BASE_URL = "https://www.indeed.com/"


    def _init__(self, html_page):
        """ Initializes the data."""
        super()._init__(html_page)

    def extract_job_results(self):
        # print(self.html_page)
        i = 0
        # Iterate through all job results for Indeed (on the first page).
        for job_row in self.html_page.find_all(name="div", attrs={"data-tn-component": "organicJob"}):
            company = job_row.find(name="span", attrs={"class", "company"}).text.strip()
            location = job_row.find(name="span", attrs={"class", "location"}).text.strip()
            title_and_url = job_row.find(name="a", attrs={"data-tn-element", "title"})
            title = title_and_url.title.strip()






            i += 1
        print(i)
