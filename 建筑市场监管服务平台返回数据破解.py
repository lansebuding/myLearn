"""
url:https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list?pg=0&pgsz=15&total=0
破解返回列表数据加密

"""

import requests
import execjs

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
    "pgsz":'15',
    "total":'450'
}

res = requests.get(url=url,params=data,cookies=cookies,headers=headers)
code = open('./监管.js',encoding='utf-8').read()
datas = execjs.compile(code).call('b',res.text)
print(datas)