# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from pymongo import MongoClient
import pymysql
# client = MongoClient()
# collection = client["tencent"]["hr"]


class TencentPipeline(object):

    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            db='tencent_hr',
            user='root',
            password='root',
            charset='utf8',
        )
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print(item)
        # sql语句
        insert_sql = """
        insert into hr(PostName,Country,Location,Category,Responsibility,LastUpdateTime) VALUES (%s,%s,%s,%s,%s,%s)
        """

        # 执行插入数据到数据库
        self.cursor.execute(
            insert_sql,
            (
                item["PostName"],
                item['Country'],
                item['Location'],
                item['Category'],
                item['Responsibility'],
                item['LastUpdateTime'],
            )
        )
        # 提交，否则无法保存到数据库
        self.conn.commit()

    # def close_spider(self, spider):
    #     # 关闭游标和链接
    #     self.cursor.close()
    #     self.conn.close()
