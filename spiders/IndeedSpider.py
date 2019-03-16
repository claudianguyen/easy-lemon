from items import JobInfo
from utils import FormatUtils, ParseUtils

from scrapy import Spider, Request
from urllib.parse import urljoin

import logging
import re


class IndeedSpider(Spider):
    name = "indeed_spider"
    BASE_URL = "https://www.indeed.com/"

    def __init__(self, url=None, num_results=None):
        """
        Handle arguments passed in by the caller.
        :param url: Desired url to start scraping.
        :param num_results: Desired number of results to process.
        """
        self.start_url = url
        self.num_results = int(num_results)
        self.found_jobs = []
        self.selected_jobs = []
        super(IndeedSpider, self).__init__()

    def start_requests(self):
        yield Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # Fetch the job results on the fetched page of the job query.
        job_results = response.css('div[data-tn-component="organicJob"]')

        # Grab basic info for jobInfo based on the results page.
        for job_row in job_results:
            job_info = self.setup_job_info(job_row)
            self.found_jobs.append(job_info)

        next_button = response.xpath('//div[@class="pagination"]//a[contains(span, "Next")]/@href').extract_first()
        if next_button and (len(self.found_jobs) < self.num_results):
            yield response.follow(next_button, self.parse)
        else:
            # Finished scraping the results, so now scrape the description pages.
            for job_info in self.found_jobs:
                yield Request(url=job_info['jobUrl'], callback=self.parse_job_description, meta={'job_info': job_info})

    def setup_job_info(self, job_row):
        """
        Returns and sets up the initial jobInfo acquired from the results page.
        :param job_row: a row from the job results page.
        :return: jobInfo
        """
        job_info = JobInfo()

        # Parse company name. Since the name might be in the href or just the span, we need to check both.
        job_href = job_row.xpath('.//span[@class="company"]//a//text()').extract_first()
        job_text = job_row.xpath('.//span[@class="company"]//text()').extract_first()
        job_info['jobCompany'] = job_text if job_text and job_text.strip() else job_href
        # Parse listed location from result.
        job_info['jobLocation'] = job_row.xpath('.//span[@class="location"]//text()').extract_first()
        # Grab job title.
        job_info['jobTitle'] = job_row.xpath('.//a[@data-tn-element="jobTitle"]/@title').extract_first()
        # Since Indeed's urls are relative urls, we need to join them with the domain to acquire the absolute url.
        job_info['jobUrl'] = \
            urljoin(self.BASE_URL, job_row.xpath('.//a[@data-tn-element="jobTitle"]/@href').extract_first())
        # Parse salary information, if available.
        job_info['jobSalary'] = \
            job_row.xpath('.//div[@class="salarySnippet"]//span[@class="salary no-wrap"]//text()').extract_first()

        # Initial defaults.
        job_info['jobPoints'] = "0"

        # Format job_info.
        FormatUtils.format_job_info(job_info)
        return job_info

    def parse_job_description(self, response):
        """
        Parses the job description.
        The job_info will be passed in via the response's meta tag.
        :return:
        """
        # Text for the "Apply Now" button that links the user to the application site.
        indeed_apply_now_text = "Apply Now"

        job_info = response.meta.get('job_info')
        # Update url to be the company website.
        direct_url = response.xpath('.//a[contains(text(), \"' + indeed_apply_now_text + '\")]/@href')\
            .extract_first()
        # Update url if direct link to job application exists.
        if direct_url is not None:
            job_info['jobUrl'] = direct_url
        job_info['jobExp'] = ''
        job_bullets = response.xpath('//li').extract()
        for bullet in job_bullets:
            exp = re.findall(ParseUtils.NUM_YEARS_EXP_REGEX, bullet)
            if exp and exp[0]:
                # Must be a number since we parsed it.
                job_info['jobExp'] = exp[0]
                job_info['jobPoints'] = "1"
                break
        FormatUtils.format_job_info(job_info)
        self.selected_jobs.append(job_info)
        yield job_info

