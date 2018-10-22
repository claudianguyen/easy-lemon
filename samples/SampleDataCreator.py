
from bs4 import BeautifulSoup
import requests
from entities.JobInfo import JobInfo
import time


class SampleDataCreator:
    """ Represents a parser. Want to parse each result. """

    def __init__(self):
        """Initializes the data."""
        self.jobs = []
        self.job_site = None

    def create_description_files(self, jobs, job_site):
        """
        Creates a html file for each job description.
        Saves html output in /Samples directory
        :return: void
        """
        i = 0
        for job in jobs:
            url = job.get_job_url()
            description_page = requests.get(url)

            # Open a file
            file_name = "samples/" + job_site + "/descriptions/description" + str(i) + ".html"
            fo = open(file_name, "w")
            fo.write(description_page.text)

            print("Writing to " + file_name + ": " + url)

            # Close opened file
            fo.close()
            i += 1

            # wait for 3 seconds until the next iteration
            time.sleep(3)




