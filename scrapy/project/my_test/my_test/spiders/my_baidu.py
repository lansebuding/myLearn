from random import random
import scrapy
import json,random
# from my_test import items
from my_test.items import MyTestItem

from scrapy import cmdline
from scrapy.utils import log

class MyBaiduSpider(scrapy.Spider):
    name = "my_baidu"
    # allowed_domains = ["www.baidu.com"]
    # allowed_domains = ["huya.com"]
    allowed_domains = ['*']
    # start_urls = ["https://www.baidu.com"]
    # start_urls = ["https://live.huya.com/liveHttpUI/getLiveList?iGid=862&iPageNo=1&iPageSize=120"]
    start_urls=['http://www.cninfo.com.cn/new/index/loadTbTrade']

    def start_requests(self):
        pass
        # for i in range(1,2):
        #     url = f'https://live.huya.com/liveHttpUI/getLiveList?iGid=862&iPageNo={i}&iPageSize=120'
        #     yield scrapy.Request(url=url,callback=self.parse)

        # post请求
        # mete是信息传递
        # dont_filter=True 不去重
        dic = {'page':1,'pagesize':10}
        yield scrapy.Request(url='http://www.cninfo.com.cn/new/index/loadTbTrade',method='POST',body=json.dumps(dic),callback=self.parse,meta={'page':random.randint(100,200)},dont_filter=True)

    def parse(self, response):
        # item=MyTestItem()
        # item['content'] = response.text
        log.logger.warning(response.url)
        print(response.text)
        print(response.meta['page'])
        # return item

    def after(self,response):
        log.logger.warning(response.url)
        print(response.text)