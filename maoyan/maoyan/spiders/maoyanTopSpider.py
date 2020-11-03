# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from maoyan.items import MaoyanItem
from scrapy import Request

class MaoYanTopSpider(Spider):
    name = 'maoyan_movie_top'
    #start_urls = ['https://maoyan.com/board/4?offset=0']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    def start_requests(self):
        url = 'https://maoyan.com/board/4'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = MaoyanItem()
        movies = response.xpath('//dl[@class="board-wrapper"]/dd')
        print(response.text)
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/i/text()'
            ).extract()[0]
            item['name'] = movie.xpath(
                './/p[@class="name"]/a/text()'
            ).extract()[0]
            item['star'] = movie.xpath(
                './/p[@class="star"]/text()'
            ).extract()[0]
            item['releasetime'] = movie.xpath(
                './/p[@class="releasetime"]/text()'
            ).extract()[0]
            yield item

        # next_url = response.xpath(
        #     '//ul[@class="list-pager"]/li/a[contains(text(),"下一页")]/@href'
        # ).extract()
        # print(next_url,type(next_url))
        # if next_url:
        #     next_url = 'https://maoyan.com/board/4' + next_url[0]
        #     yield Request(next_url, headers=self.headers)

            a = response.xpath('//ul[@class="list-pager"]/li/a/@href').extract()[-1]
            yield response.follow(a, callback=self.parse)
