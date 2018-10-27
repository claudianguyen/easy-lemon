class BaseUrlCreator:
    """Represents a url creator. """

    # Defined parameters
    salary = 0
    white_space = " "

    def __init__(self, job_title, job_location, job_salary=None):
        """Initializes the data."""
        self.job_title = job_title
        self.job_location = job_location
        self.job_salary = job_salary

    def generate_url(self):
        """
        Entry point for the UrlCreator.
        :return: A string of the url to scrape.
        """
        return "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10"

    def parse_job_title(self, string_to_replace, symbol):
        """
        Shared method that parses the job_title given to the UrlCreator. Replaces the whitespace with the given symbol.
        :return: String that represents the query parameter for the url.
        """
        return self.job_title.replace(string_to_replace, symbol)

    def parse_job_location(self, string_to_replace, symbol):
        """
        Shared method that parses the job_location given to the UrlCreator. Replaces the whitespace with the given symbol.
        :return: String that represents the query parameter for the url.
        """
        return self.job_location.replace(string_to_replace, symbol)
