from lemon_peeler.lemon_peeler.items import JobInfo
from utils import FormatUtils

from scrapy import Spider, Request
from urllib.parse import urljoin


class IndeedSpider(Spider):
    name = "indeed_spider"
    BASE_URL = "https://www.indeed.com/"

    def __init__(self, *args):
        """
        Handle arguments passed in by the caller.
        :param args: Passed in arguments to the spider.
        """
        params = args[0]
        # start_url: Url to start scraping.
        start_url = params[0]

        # num_results: Desired number of results to process.
        num_results = params[1]
        self.start_url = start_url
        self.num_results = int(num_results)
        self.found_jobs = []
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

        # Find next button.
        next_button = response.xpath('//div[@class="pagination"]//a[contains(span, "Next")]/@href').extract_first()
        if next_button and (len(self.found_jobs) < self.num_results):
            yield response.follow(next_button, self.parse)
        else:
            print(self.found_jobs)
            print(len(self.found_jobs))
            yield self.found_jobs

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
        job_info['job_company'] = job_text if job_text and job_text.strip() else job_href
        # Parse listed location from result.
        job_info['job_location'] = job_row.xpath('.//span[@class="location"]//text()').extract_first()
        # Grab job title.
        job_info['job_title'] = job_row.xpath('.//a[@data-tn-element="jobTitle"]/@title').extract_first()
        # Since Indeed's urls are relative urls, we need to join them with the domain to acquire the absolute url.
        job_info['job_url'] = \
            urljoin(self.BASE_URL, job_row.xpath('.//a[@data-tn-element="jobTitle"]/@href').extract_first())
        # Parse salary information, if available.
        job_info['job_salary'] = \
            job_row.xpath('.//td[@class="snip"]/div/span[@class="no-wrap"]//text()').extract_first()

        # Format job_info.
        FormatUtils.format_job_info(job_info)
        return job_info
