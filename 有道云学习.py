import requests
import execjs
import time
import json

cookies = {
    'OUTFOX_SEARCH_USER_ID_NCOO': '2094177160.0451846',
    'OUTFOX_SEARCH_USER_ID': '688645544@113.128.240.98',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=2094177160.0451846; OUTFOX_SEARCH_USER_ID=688645544@113.128.240.98',
    'Origin': 'https://fanyi.youdao.com',
    'Pragma': 'no-cache',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

time_now = int(round(time.time()*1000))
code1 = open('./有道云sign破解.js','r',encoding='utf-8').read()
params = execjs.compile(code1).call('main',time_now)

inputs = input('请输入需要翻译的文字：')
data = {
    'i': inputs,
    'from': 'auto',
    'to': '',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': params,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': time_now,
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}
response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)

code = open('./有道云返回密码破解.js','r',encoding='utf-8').read()
res = execjs.compile(code).call('fn',response.text)

new_res = json.loads(res)
print(new_res)
print(new_res['translateResult'][0][0]['tgt'])