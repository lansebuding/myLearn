import scrapy
import json
# from my_test import items
from my_test.items import MyTestItem

from scrapy import cmdline
from scrapy.utils import log

class MyBaiduSpider(scrapy.Spider):
    name = "my_baidu"
    # allowed_domains = ["www.baidu.com"]
    allowed_domains = ["huya.com"]
    # start_urls = ["https://www.baidu.com"]
    start_urls = ["https://live.huya.com/liveHttpUI/getLiveList?iGid=862&iPageNo=1&iPageSize=120"]

    def start_requests(self):
        for i in range(1,2):
            url = f'https://live.huya.com/liveHttpUI/getLiveList?iGid=862&iPageNo={i}&iPageSize=120'
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        item=MyTestItem()
        item['content'] = response.text
        log.logger.warning(response.url)
        return item
