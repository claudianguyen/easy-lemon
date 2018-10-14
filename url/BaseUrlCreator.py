class BaseUrlCreator:
    """Represents a url creator. """

    # Defined parameters
    salary = 0

    def __init__(self, job_title, job_location, job_salary):
        """Initializes the data."""
        self.job_title = job_title
        self.job_location = job_location
        self.job_salary = job_salary

    def generate_url(self):
        return "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10"

    def parse_job_title(self):
        """
        Shared method that parses the job_title given to the UrlCreator. Replaces the whitespace with a "+" symbol.
        :return: String that represents the query parameter for the url.
        """
        return self.replace_space_with_plus_sign(self.job_title)

    def parse_job_location(self):
        """
        Shared method that parses the job_location given to the UrlCreator. Replaces the whitespace with a "+" symbol.
        :return: String that represents the query parameter for the url.
        """
        return self.replace_space_with_plus_sign(self.job_location)

    def replace_space_with_plus_sign(self, string_to_replace):
        return string_to_replace.replace(" ", "+")