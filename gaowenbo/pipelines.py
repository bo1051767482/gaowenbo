# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import pymongo
class GaowenboPipeline(object):
    def process_item(self, item, spider):
        return item

class StatsPipeline(object):
    def __init__(self):
        #打开一个csv文件，其中newline = ""可避免写入的数据每行的空行
        self.file=open('./stats.csv', 'a',newline = "")
        self.csvwriter = csv.writer(self.file, delimiter=',')
        #写入首行的数据，即每列的标题
        self.csvwriter.writerow(['prov_code', 'prov_name', 'city_code', 'city_name', 'county_code',
                                 'county_name','town_code','town_name','village_code','village_name'])

        self.client=pymongo.MongoClient('localhost')
        self.db=self.client['crawl']
        self.table=self.db['stats']

    def process_item(self, item, spider):
        self.csvwriter.writerow((item['prov_code'],item['prov_name'], item['city_code'],item['city_name'],
                                 item['county_code'],item['county_name'],item['town_code'],
                                 item['town_name'],item['village_code'],item['village_name'],))
        self.table.insert(dict(item))
        return item

    def close_spider(self,spider):
        self.file.close()