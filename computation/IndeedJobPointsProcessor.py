from computation.BaseJobPointsProcessor import BaseJobPointsProcessor

from utils import FormatUtils


class IndeedJobPointsProcessor(BaseJobPointsProcessor):
    """ Represents a processor that computes the "job_points" for Indeed. """

    def compute_job_result_priority(self, job_result, job_query):
        """
        Computes a "point-value" for the given job_result, which will be used for prioritization of the job_results.
        :param job_result: The job_result to prioritize.
        :param job_query: The job_query that the user provided.
        :return: Point value for this job_result.
        """

        return super().compute_exp_points(job_result, job_query)

    def compute_exp_points(self, exp, job_query):
        """
        Computes the "point-value" for the given number of years of experience.
        :param exp: Raw string representing the number of years of experience.
        :param job_query: Job_query provided by the user.
        :return: Point value for the given number of years of experience.
        """
        desired_exp = 2
        if exp == "N/A":
            return 0
        # Years of experience might be a range, so parse out the hyphen.
        years_of_exp = exp.split('-')
        # May contain a '+', so replace that with whitespace.
        exp_low = years_of_exp[0].replace('+', '').strip()
        if len(years_of_exp) > 1:
            exp_high = years_of_exp[1].replace('+', '').strip()
        exp_number = int(exp_low)
        # points = 0.2 - abs(exp_number - desired_exp) / 50
        points = 1 - abs(exp_number - desired_exp) / 50
        return points

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
        if salary == "N/A" or job_query.get_job_salary() is None:
            return 0.5
        try:
            desired_salary = int(FormatUtils.currency_string_to_basic_string(job_query.get_job_salary()))
            # For now, we bank on the low side of the salary.
            salary_range = salary.split('-')
            if len(salary_range) > 1:
                salary_range[0] = FormatUtils.currency_string_to_basic_string(salary_range[0])
                # Second number represents range, may have additional characters after it. We should remove these.
                salary_range[1].split()
                salary_number_high = int(FormatUtils.currency_string_to_basic_string(salary_range[1][0].strip()))
                salary_number_low = int(salary_range[0])
                return 1 \
                    if (salary_number_low and salary_number_low > desired_salary or salary_number_high > desired_salary) \
                    else 0

            else:
                salary_number = int(salary_range[0].replace(',', '').strip())
                return 1 if salary_number and salary_number > desired_salary else 0
        except ValueError:
            return 0.5

