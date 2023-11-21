"""

Scheduler（调度器）：一个队列，用于存放requests请求

Downloader（下载器）：用于发送请求

spider（爬虫）：用于解析，处理数据

ItemPipeline（管道）：用于保存数据

Downloader Middlewares（下载器中间件）：自定义下载扩展，比如设置代理

spider Middlewares（爬虫中间件）：自定义requests请求和response过滤

"""

"""
  scrapy startproject my_baidu

  cd 进去

  scrapy genspider my_baidu https://www.baidu.com 

  ROBOTSTXT_OBEY = False

  管道注释放开

  scrapy crawl my_baidu 启动

"""

"""
scrapy shell 目标网址
res = response
使用xpath调试
res.xpath('//p/text()').getall()

res.xpath('//div[@class="pic"]/@style').getall()
"""