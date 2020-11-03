# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    PostName = scrapy.Field()  # 职位名称
    Country = scrapy.Field()  # 国家
    Location = scrapy.Field()  # 工作地点（city）
    Category = scrapy.Field()
    Responsibility = scrapy.Field()
    LastUpdateTime = scrapy.Field()
