# -*- coding: utf-8 -*-

from computation.IndeedJobPointsProcessor import IndeedJobPointsProcessor

import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EasyLemonPipeline(object):
    """
    This part of the pipeline deals with computing the "job_points" for each parsed job_info.
    """
    def process_item(self, item, spider):
        indeed_points_processor = IndeedJobPointsProcessor()
        with open("job_query.txt", "r") as job_query_file:
            job_query = json.load(job_query_file)
        job_query_file.close()
        item["jobPoints"] = 0
        computed_points = indeed_points_processor.compute_job_result_priority(item, job_query)
        item["jobPoints"] = computed_points
        return item
