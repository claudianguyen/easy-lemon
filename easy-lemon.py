#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Defined classes
from url.IndeedUrlCreator import IndeedUrlCreator

import requests
from bs4 import BeautifulSoup

# import pandas as pd
# import time


print("Hello World")
print ("Creating url...")
url = IndeedUrlCreator("software engineer", "San Francisco", "120,000")

# conducting a request of the stated URL above:
print("Creating url: " + url.generate_url())
page = requests.get(url.generate_url())

# specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")

# printing soup in a more structured tree format that makes for easier reading
# print(soup.prettify())




