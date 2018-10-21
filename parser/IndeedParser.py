from parser.BaseParser import BaseParser

class IndeedParser(BaseParser):
    """Represents a parser for Indeed. """
    def __init__(self, html_page):
        """Initializes the data."""
        super().__init__(html_page)