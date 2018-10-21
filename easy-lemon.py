#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Defined classes
from url.IndeedUrlCreator import IndeedUrlCreator
from parse.IndeedParser import IndeedParser

# External libraries
from bs4 import BeautifulSoup
import requests

# import pandas as pd
# import time

# Core logic that does the actual searching/parsing.
print("Hello World")
print ("Creating url...")
indeed_url_creator = IndeedUrlCreator("software engineer", "San Francisco", "120,000")

# conducting a request of the stated URL above:
print("Creating Indeed url: " + indeed_url_creator.generate_url())
#indeed_page = requests.get(indeed_url_creator.generate_url())

# specifying a desired format of “page” using the html parser - this allows python to read the various components
# of the page, rather than treating it as one long string.

indeed_page_sample = ""

with open("samples/indeedSearchResults.html", "r") as indeed_file:
    indeed_page_sample = indeed_file.read()

# indeed_soup = BeautifulSoup(indeed_page.text, "html.parser")
indeed_soup = BeautifulSoup(indeed_page_sample, "html.parser")

# printing soup in a more structured tree format that makes for easier reading
# print(indeed_soup.prettify())
indeed_parser = IndeedParser(indeed_soup)
indeed_parser.extract_job_results()
indeed_job_results = indeed_parser.get_job_results()
print(indeed_job_results)

# Extract url


