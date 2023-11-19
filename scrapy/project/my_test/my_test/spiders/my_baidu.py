import scrapy
# from my_test import items
from my_test.items import MyTestItem

class MyBaiduSpider(scrapy.Spider):
    name = "my_baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        item=MyTestItem()
        item['content'] = response.text
        return item
