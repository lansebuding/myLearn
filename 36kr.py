import execjs

code = open('./rsa.js','r',encoding='utf8').read()
x = execjs.compile(code)

i1 = input('输入账号：')
i2 = input('输入密码：')

i1 = x.call('encrypt')
i2 = x.call('encrypt')
import requests
import time

# now_time = int(round(time.time()*1000))

cookies = {
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218b8ffa419280e-025911bf40a3c1-26031151-2073600-18b8ffa4193807%22%2C%22%24device_id%22%3A%2218b8ffa419280e-025911bf40a3c1-26031151-2073600-18b8ffa4193807%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'Hm_lvt_713123c60a0e86982326bae1a51083e1': '1698927625,1699010640',
    'Hm_lpvt_713123c60a0e86982326bae1a51083e1': '1699010640',
    'Hm_lvt_1684191ccae0314c6254306a8333d090': '1698927625,1699010640',
    'Hm_lpvt_1684191ccae0314c6254306a8333d090': '1699010640',
    'aliyungf_tc': 'e77e23dbcfdcd24a61d35304e0e48265c0bf2efd63dbecef89243ba381a3fce6',
    'acw_tc': '1a0c398516990106509631342ebeb1dfb8be0b330b12e7d4be84d9fdf2d47e',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218b8ffa419280e-025911bf40a3c1-26031151-2073600-18b8ffa4193807%22%2C%22%24device_id%22%3A%2218b8ffa419280e-025911bf40a3c1-26031151-2073600-18b8ffa4193807%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_713123c60a0e86982326bae1a51083e1=1698927625,1699010640; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1699010640; Hm_lvt_1684191ccae0314c6254306a8333d090=1698927625,1699010640; Hm_lpvt_1684191ccae0314c6254306a8333d090=1699010640; aliyungf_tc=e77e23dbcfdcd24a61d35304e0e48265c0bf2efd63dbecef89243ba381a3fce6; acw_tc=1a0c398516990106509631342ebeb1dfb8be0b330b12e7d4be84d9fdf2d47e',
    'Origin': 'https://36kr.com',
    'Pragma': 'no-cache',
    'Referer': 'https://36kr.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'krtoken': '',
    'partner_id': 'web',
    'timestamp': time.time()*1000,
    'param': {
        'countryCode': '86',
        'mobileNo': i1,
        'password': i2,
    },
}

response = requests.post(
    'https://gateway.36kr.com/api/mus/login/byMobilePassword',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)