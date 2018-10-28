class JobInfo:
    def __init__(self, job_title, job_location, job_url, job_company, job_salary):
        self.job_info = \
            {"title": job_title,
             "location": job_location,
             "url": job_url,
             "company": job_company,
             "salary": job_salary}

    def get_job_title(self):
        """
        Gets the job title
        :return: string
        """
        return self.job_info["title"]

    def get_job_location(self):
        """
        Gets the location
        :return: string
        """
        return self.job_info["location"]

    def get_job_url(self):
        """
        Gets the url to job description
        :return: string
        """
        return self.job_info["url"]

    def get_job_company(self):
        """
        Gets the company that is hiring.
        :return: string
        """
        return self.job_info["location"]

    def get_job_salary(self):
        """
        Gets the salary of the job (if applicable)
        :return: string
        """
        return self.job_info["salary"]

    def __str__(self):
        """
        Updated str() method so we format JobInfo as a dictionary.
        :return: string representation of a dictionary.
        """
        return str(self.job_info)

    def __repr__(self):
        """
        JobInfo should be represented as a dictionary.
        :return: string representation of a dictionary.
        """
        return repr(self.job_info)
