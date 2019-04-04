# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from computation.IndeedJobPointsProcessor import IndeedJobPointsProcessor
from db.JobQueryService import JobQueryService
from entities.JobQuery import JobQuery

import pymongo


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# Pipeline for the IndeedSpider.
class IndeedPipeline(object):
    """
    This part of the pipeline deals with computing the "job_points" for each parsed job_info.
    """
    collection_name = 'job_queries'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        # Opens up a db connection when initializing spider.
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        indeed_points_processor = IndeedJobPointsProcessor()
        # job_query_service = JobQueryService(os.environ.get("MONGO_DB_CLIENT_CREDS"))
        job_query_entity = self.db[self.collection_name].find_one(ObjectId(spider.job_query_id))

        job_query = JobQuery(job_query_entity)
        item["job_points"] = 0
        computed_points = indeed_points_processor.compute_job_result_priority(item, job_query)
        item["job_points"] = computed_points
        return item


class MongoDBPipeline(object):
    """
    Pipeline for saving items to MongoDB
    """
    collection_name = 'job_results'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        # Opens up a db connection when initializing spider.
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
