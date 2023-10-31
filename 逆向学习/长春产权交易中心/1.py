# import requests
from curl_cffi import requests
import execjs
responseCode = open('./逆向学习/长春产权交易中心/1.js','r',encoding='utf8').read()


param = execjs.compile(responseCode).call('main',{"page":2})

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/xml;charset=UTF-8',
    'Origin': 'https://www.ccprec.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.ccprec.com/navCqzr/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = param

response = requests.post('https://www.ccprec.com/honsanCloudAct', headers=headers, data=data,impersonate='chrome100')

x = execjs.compile(responseCode).call('de',response.text)
print(x)