class UrlCreator:
    """Represents a url creator. """

    # Defined parameters
    salary = 0

    def __init__(self, site):
        """Initializes the data."""
        self.site = site

    def create_url(self):
        return "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start=10"
