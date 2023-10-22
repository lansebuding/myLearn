import requests
import execjs

cookies = {
    'btoken': 'OESY2VAYSNUCXY7AEWB3955DL9VZ02CE',
    'hy_data_2020_id': '18b523826e2bbf-09a2fe78e1e7cd-26031151-2073600-18b523826e3521',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218b523826e2bbf-09a2fe78e1e7cd-26031151-2073600-18b523826e3521%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218b523826e2bbf-09a2fe78e1e7cd-26031151-2073600-18b523826e3521%22%7D',
    'sajssdk_2020_cross_new_user': '1',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'btoken=OESY2VAYSNUCXY7AEWB3955DL9VZ02CE; hy_data_2020_id=18b523826e2bbf-09a2fe78e1e7cd-26031151-2073600-18b523826e3521; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218b523826e2bbf-09a2fe78e1e7cd-26031151-2073600-18b523826e3521%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218b523826e2bbf-09a2fe78e1e7cd-26031151-2073600-18b523826e3521%22%7D; sajssdk_2020_cross_new_user=1',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
jsCode = open('./烯牛参数.js','r',encoding='utf-8').read()
params = execjs.compile(jsCode).call('main')
json_data = {
    'payload': params['payload'],
    'sig': params['sig'],
    'v': 1,
}
print(params)
response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()

jsCode1 = open('./烯牛返回参数解析.js','r',encoding='utf-8').read()
params1 = execjs.compile(jsCode1).call('main',response['d'])

print(params1)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"payload":"LBc3V0I6ZGB5bXsxTCQnPRBuBAQVcDhbICcmb2x3AjI=","sig":"CE704F132C4E47B31E91773020275904","v":1}'
#response = requests.post(
#    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)