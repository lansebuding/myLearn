import requests
import execjs

cookies = {
    'Hm_lvt_1521e0fb49013136e79181f2888214a7': '1697958373',
    'Hm_lpvt_1521e0fb49013136e79181f2888214a7': '1697958373',
    'JSESSIONID': '02020BBB2F4B1368C8DAC28C3E139FAF',
    '_ACCOUNT_': 'NDJkNWRiNjllODg5NGU1ZDk2MmQ5OWMzYjg1NTAzNWMlNDAlNDBtb2JpbGU6MTY5OTE3MjUwNDQ0NTpiMTI2OGMwMGJiYjI2NDAxOWVhMTkxODVhNDdlMjZkNQ',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Auth-Plus': '',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_1521e0fb49013136e79181f2888214a7=1697958373; Hm_lpvt_1521e0fb49013136e79181f2888214a7=1697958373; JSESSIONID=02020BBB2F4B1368C8DAC28C3E139FAF; _ACCOUNT_=NDJkNWRiNjllODg5NGU1ZDk2MmQ5OWMzYjg1NTAzNWMlNDAlNDBtb2JpbGU6MTY5OTE3MjUwNDQ0NTpiMTI2OGMwMGJiYjI2NDAxOWVhMTkxODVhNDdlMjZkNQ',
    'Origin': 'https://www.hanghangcha.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'clientInfo': 'web',
    'clientVersion': '1.0.2',
    'currentHref': 'https://www.hanghangcha.com/products-local',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'filter': '{"city":"","lv":null,"province":"","userId":4779180,"companyId":null,"limit":20,"skip":0,"keyword":null,"companyType":"local","industry":""}',
}
response = requests.get('https://api.hanghangcha.com/hhc/invest/getProduct', params=params, cookies=cookies, headers=headers).json()

jsCode = open('./行行查返回数据解析.js','r',encoding='utf-8').read()
params = execjs.compile(jsCode).call('main',response['data'])

print(type(params))
print(params)