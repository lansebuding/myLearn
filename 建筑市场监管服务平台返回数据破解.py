"""
url:https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list?pg=0&pgsz=15&total=0
破解返回列表数据加密

"""

import requests

url = 'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list'

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1697541179,1697601549',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1697601555',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Accesstoken':'',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Sec-Ch-Ua': '\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '\"Windows\"',
    'Timeout':'30000',
    'Host':'jzsc.mohurd.gov.cn'
}

data = {
    "pg":'0',
    "pgsz":'0',
    "total":'0'
}

res = requests.get(url=url,params=data,cookies=cookies,headers=headers)
res.encoding='utf-8'

# print(res.text)

# 进行解密，本次获取的数据是使用AES CBC模式进行加密的

key = 'jo8j9wGw%6HbxfFn'.encode() # 秘钥
iv = '0123456789ABCDEF'.encode()  # 偏移量

import base64
from Crypto.Util import Padding
from Crypto.Cipher import AES
from binascii import a2b_hex,b2a_hex
import json

aes = AES.new(key,AES.MODE_CBC,iv=iv)

data1 = aes.decrypt(a2b_hex(res.text)).decode()

data1=data1[19:]
data1=data1[:-34]

# print(data1)
newList = list(json.loads(data1)['list'])

for i in newList:
    print(f'名字是：{i["QY_FR_NAME"]}，公司名字是：{i["QY_NAME"]}')