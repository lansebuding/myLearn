# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyTestPipeline:
    def process_item(self, item, spider):
        self.open_file(spider)
        self.file.write(item['content'])
        self.close_file(spider)
        return item


    def open_file(self, spider):
        self.file = open('./htmls/t.json','a',encoding='utf-8')

    def close_file(self, spider):
        self.file.close()