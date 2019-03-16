# -*- coding: utf-8 -*-

from computation.IndeedJobPointsProcessor import IndeedJobPointsProcessor

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
        item["jobPoints"] = 0
        computed_points = indeed_points_processor.compute_exp_points(item["jobExp"], item["jobSalary"])
        item["jobPoints"] = computed_points
        return item
