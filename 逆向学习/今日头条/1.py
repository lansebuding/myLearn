import requests,json,datetime,time

dic = {
    'url':f'https://www.toutiao.com/api/pc/list/feed?channel_id=0&min_behot_time={time.time()}&offset=0&refresh_count=1&category=pc_profile_recommend&aid=24&app_name=toutiao_web'
}
param={
    'group':'t',
    'name':'test',
    'action':'fn',
    'param':json.dumps(dic)
}
res = requests.get('http://127.0.0.1:12080/go',params=param).json()
_signature = json.loads(res['data'])
print(dic['url'])

cookies = {
    'msToken': 'lvzMaBOqs9vCrp8O2iB6MEQqQFgICIctyWQkWOieUoPiZRv1xgnu4XIeJ4jAPclF3Vdszo5bBpjZ622ACzYP1mRHYZDlqhio2qmqoEXj',
    '__ac_signature': '_02B4Z6wo00f01yygRtwAAIDDrKK8nue.Ip8sgEJAAK5sf0',
    'tt_webid': '7298600032726320649',
    'ttcid': '58f3908256cd45999cd52350ae05c82e86',
    '_ga': 'GA1.1.67411074.1699337758',
    'local_city_cache': '%E6%B5%8E%E5%8D%97',
    'csrftoken': '19e8e9d6ea5eee5f34ab1b99f308f45c',
    's_v_web_id': 'verify_lonxtqby_Cgk6c8MS_B5sS_4JcR_9zLV_XBOlGxNXLyNV',
    '_ga_QEHZPBE5HH': 'GS1.1.1699517504.4.0.1699517504.0.0.0',
    'tt_scid': 'oC4ij9SATSj6v7559w1-HGFGBxSasfQPrYmbozYw8PEPqBZLBhyXdG1MiJ92wbey0fc2',
    'ttwid': '1%7CZwuRdA_McnwRw5wQqszzt8IheDRe6hz71vzB48VG-is%7C1699517504%7C835210af69ddb76a0abd5b8c8e4ce3b2f371ff79fca8c19536c90b77a632c23a',
}

headers = {
    'authority': 'www.toutiao.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.toutiao.com/?wid=1699337755879',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}


response = requests.get(dic['url']+'&_signature='+_signature, cookies=cookies, headers=headers).json()
print(_signature)
print(response)