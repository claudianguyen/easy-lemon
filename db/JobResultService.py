# -*- coding: utf-8 -*-

import pymongo
from bson.objectid import ObjectId


class JobResultService(object):
    """
    Accesses database to find/update job_queries.
    """

    def __init__(self, creds):
        client = pymongo.MongoClient(creds)
        db = client.easy_lemon
        self.job_results = db.job_results

    def find_job_results_by_query_id(self, job_query_id):
        """
        Finds the job_query with the given job_query_id
        :param job_query_id: Id that was used when creating the entity.
        :return: Cursor object containing all job_results with the given id in a decreasing order.
        """
        return self.job_results.find({"job_query_id": job_query_id}, {"_id": 0, "job_query_id": 0})\
            .sort([('job_points', -1)])

    def insert_job_result(self, job_result):
        """
        Inserts the given job_query into the db.
        :param job_result: The object to insert into the db.
        :return: job_query_id generated when inserting into db.
        """
        return self.job_results.insert_one(job_result)

    def delete_job_results_by_query_id(self, job_query_id):
        return self.job_results.remove({'job_query_id': job_query_id})
