class JobInfo:
    def __init__(self, job_title, job_location, job_url, job_company, job_salary):
        self.job_title = job_title
        self.job_location = job_location
        self.job_url = job_url
        self.job_company = job_company
        self.job_salary = job_salary

    def get_job_title(self):
        """
        Gets the job title
        :return: string
        """
        return self.job_title

    def get_job_location(self):
        """
        Gets the location
        :return: string
        """
        return self.job_location

    def get_job_url(self):
        """
        Gets the url to job description
        :return: string
        """
        return self.job_url

    def get_job_company(self):
        """
        Gets the company that is hiring.
        :return: string
        """
        return self.job_company

    def get_job_salary(self):
        """
        Gets the salary of the job (if applicable)
        :return: string
        """
        return self.job_salary
