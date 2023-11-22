from random import random
import scrapy
import json,random
# from my_test import items
from my_test.items import MyTestItem

from scrapy import cmdline
from scrapy.utils import log
import lxml
from lxml import etree
from lxml.etree import _Element
import urllib.parse as q

class MyBaiduSpider(scrapy.Spider):
    name = "my_baidu"
    # allowed_domains = ["www.baidu.com"]
    # allowed_domains = ["huya.com"]
    # allowed_domains = ['www.yiwugo.com']
    # start_urls = ["https://www.baidu.com"]
    # start_urls = ["https://live.huya.com/liveHttpUI/getLiveList?iGid=862&iPageNo=1&iPageSize=120"]
    # start_urls=['http://www.cninfo.com.cn/new/index/loadTbTrade']

    def start_requests(self):
        # pass
        params={
            "q":q.quote('奶茶'),
        }
        # for i in range(1):
        headers={
            'Accept-Language':'zh-CN'
        }
        params['cpage']=1
        for i in range(1,30):
            yield scrapy.Request(f'https://www.yiwugo.com/search/s.html?cpage={i}&q={params["q"]}&equipmentCode=540cb188-0919-48df-cdc0-e75145226014&searchMethod=original&spm=d3d3Lnlpd3Vnby5jb20v',callback=self.parse,headers=headers,meta={'page':i})

        # post请求
        # mete是信息传递
        # dont_filter=True 不去重
        # dic = {'page':1,'pagesize':10}
        # yield scrapy.Request(url='http://www.cninfo.com.cn/new/index/loadTbTrade',method='POST',body=json.dumps(dic),callback=self.parse,meta={'page':random.randint(100,200)},dont_filter=True)

    def parse(self, response):
        item=MyTestItem()
        log.logger.warning(response.url)
        my_list = self.deal_data(response.text)
        print('当前第'+str(response.meta['page'])+'页')
        item['content'] = my_list
        return item

    def after(self,response):
        log.logger.warning(response.url)
        print(response.text)

    def deal_data(self,text:str):
        h:_Element= etree.HTML(text)
        res:list = h.xpath('//div[@class="pro_list_product_img2"]')
        my_list = []
        for i in res:
            try:
                title = i.xpath('./ul/li')[0].xpath('./a[@class="productloc"]/@title')[0]
                p=i.xpath('./ul/li')[1].xpath('./span[@class="pri-left"]/em/font')
                store:list[str] = i.xpath('./ul/li')[2].xpath('./font/a/text()')
                price = p[0].text+'.'+p[1].text
                my_list.append({
                    'title':title,
                    'store':store[0],
                    'price':price
                })
            except Exception as err:
                print(err)
        return my_list