from url.BaseUrlCreator import BaseUrlCreator


class LinkedInUrlCreator(BaseUrlCreator):
    """Represents a LinkedIn url creator. """

    # Defined parameters
    salary = 0
    converted_apace_symbol = "%20"
    url_endpoint = "https://www.linkedin.com/jobs/search?keywords="

    def __init__(self, job_title, job_location):
        """Initializes the data."""
        super().__init__(job_title, job_location)

    def parse_job_location(self, string_to_convert, symbol):
        """
        Parses the job_location for LinkedIn. Adds the LinkedIn query parameter for location.
        """
        job_location = super().parse_job_location(self.white_space, self.converted_apace_symbol)
        return "&location=" + job_location

    def generate_url(self):
        """
        Url for Indeed: This will contain all the query parameters given to the IndeedUrlCreator.
        :return: String that represents a full job query on Indeed.
        """
        return self.url_endpoint \
            + self.parse_job_title(self.white_space, self.converted_apace_symbol) \
            + self.parse_job_location(None, None)
