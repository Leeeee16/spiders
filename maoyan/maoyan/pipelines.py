# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MaoyanPipeline(object):

    # def __init__(self):
    #     #连接数据库
    #     self.connect = pymysql.connect(
    #         host='127.0.0.1',
    #         port=3306,
    #         db='maoyan',
    #         user='root',
    #         passwd='123456',
    #         charset='utf8',
    #         use_unicode=True
    #     )
    #     #通过cursor执行增删查改
    #     self.cursor = self.connect.cursor()

    def __init__(self):
        pass


    def open_spider(self,spider):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            db='maoyan',
            user='root',
            passwd='123456',
            charset='utf8',
        )
        self.cursor = self.connect.cursor()

    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()


    def process_item(self, item, spider):

        self.cursor.execute(
            """insert into maoyantop(ranking , name, star, releasetime)
            values (%s, %s, %s, %s)""",
            (
                item['ranking'],
                item['name'],
                item['star'],
                item['releasetime']
            )
        )
        # self.cur.execute("insert into maoyantop values('{}','{}','{}','{}')".format(item['ranking'],item['name'],item['star'],item['releasetime']))
        # #提交sql语句
        self.connect.commit()
        return item
