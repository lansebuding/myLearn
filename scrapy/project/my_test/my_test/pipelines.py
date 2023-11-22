# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class MyTestPipeline:
    def process_item(self, item, spider):
        for i in item['content']:
            self.db.insert_one(i)
        print('down')
        return item

    def __init__(self) -> None:
        self.connect()

    def open_file(self, spider):
        self.file = open('./htmls/1.html','w',encoding='utf-8')

    def close_file(self, spider):
        self.file.close()
    
    def connect(self):
        client = pymongo.MongoClient(host='localhost',port=27017)
        db = client['test']['ppp']
        self.db = db