"""
Utils method for formatting text.
"""


def format_job_info(job_info):
    """
    Checks each characteristic in the job_info object. If the charc is None, return "N/A",
    otherwise, return the stripped text.
    :param job_info: the job_info that needs to be formatted.
    :return: job_info: this job_info will contain the formatted changes.
    """
    for charc in job_info.keys():
        job_charc = job_info[charc]
        if job_charc:
            job_info[charc] = job_charc.strip()
        else:
            job_info[charc] = "N/A"

    return job_info
