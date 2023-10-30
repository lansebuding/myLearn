# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

str1 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <ul>
      <li>444</li>
      <li>444</li>
    </ul>
    <ul>
      <li class="ppp">333</li>
      <li>4444444444</li>
    </ul>
    <p class="ppp" id="p1"><span>aaa</span></p>
    <script>
      function clc() {
        const dom = document.getElementById("ad");
        dom.play();
      }
    </script>
  </body>
</html>
"""

so = BeautifulSoup(str1,'lxml')

# print(so.p.attrs)

# print(so.find_all('li',class_='ppp'))
# print(so.select('li'))
# print(so.select('.ppp>span'))
# print(so.find_all('li'))
# print(so.find_all(class_='ppp'))

def test():
  cookies = {
      'alicfw': '1434407345%7C2014479822%7C1328233921%7C1328232928',
      'alicfw_gfver': 'v1.200309.1',
      'aliyungf_tc': 'e540c8fc4156e6dedf45feebc30d7f520651d3c77218b86a46887827220e2282',
      'acw_tc': '0a6fc6a016985455413911764ecc6589f012ac439a08f1ed725a54e186781d',
      'Hm_lvt_1684191ccae0314c6254306a8333d090': '1698545545',
      'Hm_lvt_713123c60a0e86982326bae1a51083e1': '1698545545',
      'sajssdk_2015_cross_new_user': '1',
      'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218b79342f1070f-0e63a32b6e9b21-3e604809-2073600-18b79342f11693%22%2C%22%24device_id%22%3A%2218b79342f1070f-0e63a32b6e9b21-3e604809-2073600-18b79342f11693%22%2C%22props%22%3A%7B%7D%7D',
      'Hm_lpvt_1684191ccae0314c6254306a8333d090': '1698545653',
      'Hm_lpvt_713123c60a0e86982326bae1a51083e1': '1698545653',
      'SERVERID': '6eb0a1872728d69c244094a636b7db3b|1698545738|1698545543',
  }

  headers = {
      'Connection': 'keep-alive',
      'Cache-Control': 'max-age=0',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-User': '?1',
      'Sec-Fetch-Dest': 'document',
      'Referer': 'https://36kr.com/information/web_news/latest/',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      # 'Cookie': 'alicfw=1434407345%7C2014479822%7C1328233921%7C1328232928; alicfw_gfver=v1.200309.1; aliyungf_tc=e540c8fc4156e6dedf45feebc30d7f520651d3c77218b86a46887827220e2282; acw_tc=0a6fc6a016985455413911764ecc6589f012ac439a08f1ed725a54e186781d; Hm_lvt_1684191ccae0314c6254306a8333d090=1698545545; Hm_lvt_713123c60a0e86982326bae1a51083e1=1698545545; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218b79342f1070f-0e63a32b6e9b21-3e604809-2073600-18b79342f11693%22%2C%22%24device_id%22%3A%2218b79342f1070f-0e63a32b6e9b21-3e604809-2073600-18b79342f11693%22%2C%22props%22%3A%7B%7D%7D; Hm_lpvt_1684191ccae0314c6254306a8333d090=1698545653; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1698545653; SERVERID=6eb0a1872728d69c244094a636b7db3b|1698545738|1698545543',
  }

  req = requests.get('https://36kr.com/information/web_news/latest/', cookies=cookies, headers=headers)
  # print(req.text)
  with open('./111111.html','w',encoding='utf8') as file:
    file.write(req.text)


test()