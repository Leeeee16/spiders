# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymysql


class GetWuyouPipeline(object):

    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(
            user='root',    # mysql名
            password='root',    # mysql密码
            port=3306,
            db='positions',     # 数据库名
            host='127.0.0.1',
            charset='utf8'
        )
        # 创建一个游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # print(item)  # 将数据存入数据库前输出一下item
        # sql语句
        insert_sql = """
        insert into job(`position`,company,salary,education,work_experience,workplace,place,job_requirements) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        # 执行插入语句
        self.cursor.execute(
            insert_sql,
            (
                item['position'],
                item['company'],
                item['salary'],
                item['education'],
                item['work_experience'],
                item['workplace'],
                item['place'],
                item['job_requirements'],
            )
        )

        self.conn.commit()
        # self.conn.close()
