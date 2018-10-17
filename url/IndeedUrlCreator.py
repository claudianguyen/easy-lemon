from url.BaseUrlCreator import BaseUrlCreator

class IndeedUrlCreator(BaseUrlCreator):
    """Represents a url creator. """

    # Defined parameters
    salary = 0
    url_endpoint = "https://www.indeed.com/jobs?q="

    def __init__(self, job_title, job_location, job_salary):
        """Initializes the data."""
        super().__init__(job_title, job_location, job_salary)

    def parse_job_location(self):
        """
        Parses the job_location for Indeed. Adds the Indeed query parameter for location.
        """
        job_location = super().parse_job_location()
        return "&l=" + job_location

    def parse_job_salary(self):
        """
        Parses the job_salary for Indeed. Adds any additional parameters for the Indeed salary query.
        Note: Indeed uses "%24" to signify the start of the salary query, and uses "%2C" as a delimiter for commas.
        :return: String that represents the salary parameter for an Indeed url.
        """
        return "+%24" + self.job_salary.replace(",", "%2C")

    def generate_url(self):
        """
        Url for Indeed: This will contain all the query parameters given to the IndeedUrlCreator.
        :return: String that represents a full job query on Indeed.
        """
        return self.url_endpoint + self.parse_job_title() + self.parse_job_salary() + self.parse_job_location()
