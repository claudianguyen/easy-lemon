"""
Class containing the job search parameters. This class contains user-defined parameters as well as the
different computation required.
"""


class JobQuery:

    def __init__(self, job_query):
        self.job_query = \
            {"title": job_query['title'],
             "location": job_query['location'],
             "experience": job_query['experience'],
             "salary": job_query['salary'],
             "keywords": job_query['keywords']}

    def get_job_title(self):
        """
        Gets the job title
        :return: string
        """
        return self.job_query["title"]

    def get_job_location(self):
        """
        Gets the location
        :return: string
        """
        return self.job_query["location"]

    def get_job_experience(self):
        """
        Gets the experience
        :return: string
        """
        return self.job_query["experience"]

    def get_job_salary(self):
        """
        Gets the salary of the job query (if applicable)
        :return: string
        """
        return self.job_query["salary"]

    def __str__(self):
        """
        Updated str() method so we format JobQuery as a dictionary.
        :return: string representation of a dictionary.
        """
        return str(self.job_query)

    def __repr__(self):
        """
        JobQuery should be represented as a dictionary.
        :return: string representation of a dictionary.
        """
        return repr(self.job_query)
