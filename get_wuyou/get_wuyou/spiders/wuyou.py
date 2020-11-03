# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from get_wuyou.items import GetWuyouItem


class WuyouSpider(CrawlSpider):
    name = 'wuyou'
    allowed_domains = ['search.51job.com']

    def start_requests(self):
        start_url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%2B,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=04&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        yield scrapy.Request(start_url)

    def parse(self, response):
        item = GetWuyouItem()
        urls = response.xpath('//*[@id="resultList"]/div[@class="el"]/p/span/a/@href').extract()  # 获取详情页的url
        for url in urls:  # 遍历每一页
            # url = response.xpath('//*[@id="resultList"]/div[@class="el"]/p/span/a/@href'.format(str(i))).get()
            yield scrapy.Request(url, callback=self.detail_parse,
                                 meta={'item': item},
                                 # priority=10,
                                 # dont_filter=True
                                 )
        next_url = response.xpath('//a[contains(text(),"下一页")]/@href').get()  # 获取下一页的url
        print("next_url is " + next_url)
        yield response.follow(next_url, self.parse)  # 遍历页数

    def detail_parse(self, response):
        item = response.meta['item']
        item['position'] = ''
        item['company'] = ''
        item['salary'] = ''
        item['education'] = ''
        item['work_experience'] = ''
        item['workplace'] = ''
        item['place'] = ''
        item['job_requirements'] = ''
        # 职位名称
        item['position'] = response.xpath('//div[@class="tCompany_center clearfix"]/div[2]/div/div/h1/text()').extract()

        # 公司名称
        item['company'] = response.xpath(
            '//div[@class="tCompany_center clearfix"]/div[2]/div/div/p/a[1]/text()').extract()
        # 薪水
        item['salary'] = response.xpath(
            '//div[@class="tCompany_center clearfix"]/div[2]/div/div/strong/text()').extract()
        # 学历
        item['education'] = '本科'  # 爬取学历要求为本科的职位
        # 工作经验
        work_experience = response.xpath(
            '//div[@class="tCompany_center clearfix"]/div[2]/div/div/p[2]/text()[2]').extract()[0]
        item['work_experience'] = "".join(work_experience.split())  # 去除爬取内容中出现的 \xa0
        # 工作地点
        item['workplace'] = response.xpath(
            '//div[@class="tCompany_center clearfix"]/div[3]/div[2]/div/p/text()').extract()
        # 工作地
        place = response.xpath('//div[@class="tCompany_center clearfix"]/div[2]/div/div/p[2]/text()[1]').extract()[0]
        item['place'] = "".join(place.split())
        # 工作要求
        requirements = response.xpath('//div[@class="tCompany_main"]/div[1]/div[1]/p/text()[1]').extract()
        job_requirements = ''
        for i in requirements:
            i.strip()
            job_requirements += i  # 去除多余的字符
        # item['job_requirements'] = "".join(job_requirements.split())
        item['job_requirements'] = job_requirements
        yield item
