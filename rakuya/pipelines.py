# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class RakuyaPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        scrapy_db = self.client['scrapy_db']
        self.coll = scrapy_db['rakuya_scrapy']

    def process_item(self, item, spider):
        self.coll.insert_one(item)
        return item

    def close_spider(self, spider):
        self.client.close()