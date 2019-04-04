# -*- coding: utf-8 -*-

import pymongo
from bson.objectid import ObjectId


class JobQueryService(object):
    """
    Accesses database to find/update job_queries.
    """

    def __init__(self, creds):
        client = pymongo.MongoClient(creds)
        db = client.easy_lemon
        self.job_queries = db.job_queries

    def find_job_query_by_obj_id(self, job_query_id):
        """
        Finds the job_query with the given job_query_id
        :param job_query_id: Id that was used when creating the entity.
        :return: Job_query object.
        """
        return self.job_queries.find_one(ObjectId(job_query_id))

    def insert_job_query(self, job_query):
        """
        Inserts the given job_query into the db.
        :param job_query: The object to insert into the db.
        :return: job_query_id generated when inserting into db.
        """
        return self.job_queries.insert_one(job_query)
