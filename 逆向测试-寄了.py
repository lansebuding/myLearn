import requests
import time


url = 'https://dict.youdao.com/webtranslate'

key = '习惯'

cookies = {
    'OUTFOX_SEARCH_USER_ID': '-312652410@10.108.162.134',
    'OUTFOX_SEARCH_USER_ID_NCOO': '42958927.495580636',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://fanyi.youdao.com',
    'Pragma': 'no-cache',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua': '\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\"Windows\"',
}

data = {
    'i': key,
    'from': 'auto',
    'to': '',
    'domain': '0',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': 'e1806c657b7fef10915e3d0651e3dd91',
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': '1697510383902',
    'keyfrom': 'fanyi.web',
    "min":"1",
    "screen":"1",
    "model":"1",
    "network":"wifi",
    "abtest":"0",
    "yduuid":"abcdefg"
}

response = requests.post(url, headers=headers, data=data, cookies=cookies)
response.encoding='utf-8'
print(response.text)