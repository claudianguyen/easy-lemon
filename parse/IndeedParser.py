from parse.BaseParser import BaseParser

class IndeedParser(BaseParser):
    """Represents a parse for Indeed. """


    def _init__(self, html_page):
        """Initializes the data."""
        super()._init__(html_page)