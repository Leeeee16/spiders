# -*- coding: utf-8 -*-
import json
import scrapy
from tencent.items import TencentItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    # allowed_domains = ['careers.tencent.com']

    custom_settings = {
        'DOWNLOAD_DELAY': 5
    }

    def start_requests(self):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&language=zh-cn&area=cn&pageIndex=1'
        yield scrapy.Request(url)

    def parse(self, response):
        json_dict = json.loads(response.body)
        json_Data = json_dict["Data"]
        json_Posts = json_Data["Posts"]
        item = TencentItem()
        for i in range(2, 400):
            for each in json_Posts:
                item['PostName'] = each['RecruitPostName']  # 职位名称
                item['Country'] = each['CountryName']
                item['Location'] = each['LocationName']  # 工作城市
                item['Responsibility'] = each['Responsibility']
                item['Category'] = each['CategoryName']
                item['LastUpdateTime'] = each['LastUpdateTime']
                # print(item)
                yield item
            next_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&language=zh-cn&area=cn&pageIndex=' + str(i)
            print(next_url)
            scrapy.Request(next_url)
