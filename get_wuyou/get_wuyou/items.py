# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetWuyouItem(scrapy.Item):
    position = scrapy.Field()  # 职位名称
    company = scrapy.Field()  # 公司名称
    salary = scrapy.Field()  # 薪资
    education = scrapy.Field()  # 学历
    work_experience = scrapy.Field()  # 工作经历
    workplace = scrapy.Field()  # 工作地点（具体）
    place = scrapy.Field()  # 工作城市
    job_requirements = scrapy.Field()  # 职位要求