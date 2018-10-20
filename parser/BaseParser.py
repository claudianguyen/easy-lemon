import requests
import bs4
from bs4 import BeautifulSoup

class BaseParser:
    """ Represents a parser. Want to parse each result. """

    def __init__(self, html_page):
        """Initializes the data."""
        self.html_page = html_page

    def extract_company_title(self, html_page):
        """
        Entry point for the UrlCreator.
        :return: A string of the url to scrape.
        """
        return "Ellie Mae"

