import requests

p = {
    'group':'t',
    'name':'test',
    'action':'fn'
}
res = requests.get('http://127.0.0.1:12080/go',params=p).json()



cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1698379746',
    'routeId': '.uc2',
    'MALLSSID': '6F4538487042326D794F4468514342356E586E6F476E6A6764515A7377396D6179616177306E775A35534F4663382B5462676F30704C774459794E5948775558',
    'JSESSIONID': '9455905045AE444232FDBA2035A9A539',
}

headers = {
    'Accept': '*/*',
    'Accept-EncKey': res['data'],
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1698379746; routeId=.uc2; MALLSSID=6F4538487042326D794F4468514342356E586E6F476E6A6764515A7377396D6179616177306E775A35534F4663382B5462676F30704C774459794E5948775558; JSESSIONID=9455905045AE444232FDBA2035A9A539',
    'Origin': 'http://webapi.cninfo.com.cn',
    'Referer': 'http://webapi.cninfo.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'scode': '399001',
    'market': '012002',
    'orgid': 'jysz0000001',
    'sdate': '2022-11-10',
    'edate': '2023-11-10',
}

response = requests.post(
    'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1095',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
).json()
print(res['data'])
print(response)