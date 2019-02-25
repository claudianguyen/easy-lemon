from items import JobInfo


class BaseJobPointsProcessor:
    """ Represents a processor that computes the "job_points" that should be assigned to a given job_result. """

    def compute_job_result_priority(self, job_result, job_query):
        """
        Computes a "point-value" for the given job_result, which will be used for prioritization of the job_results.
        :param job_result: The job_result to prioritize.
        :param job_query: The job_query that the user provided.
        :return: Point value for this job_result.
        """
        points = 0
        points += self.compute_salary_points(job_result['job_salary'], job_query) \
                  + self.compute_exp_points(job_result['job_exp'], job_query)
        return points

    def compute_exp_points(self, exp, job_query):
        """
        Computes the "point-value" for the given number of years of experience.
        :param exp: Raw string representing the number of years of experience.
        :param job_query: Job_query provided by the user.
        :return: Point value for the given number of years of experience.
        """
        return 0

    def compute_salary_points(self, salary, job_query):
        """
        Computes the "point-value" for the job_salary portion.
        1: greater than expected
        0.5: No salary information
        0: Below expected.
        :param salary: The salary portion saved by the job_result.
        :param job_query: The job_query provided by the user.
        :return:
        """
        return 0
