import requests
import execjs
import time
import json

# code = open('./逆向学习/百度翻译/1.js','r',encoding='utf8').read()
# sign = execjs.compile(code).call('t','睡觉')

dict={'name':'睡觉'}
p = {
    'group':'t',
    'name':'test',
    'action':'fn',
    'param':json.dumps(dict)
}
res = requests.get('http://127.0.0.1:12080/go',params=p).json()
print(res['data'])

cookies = {
    'REALTIME_TRANS_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'BIDUPSID': 'CA328BEADA915A3A3036972318E84BA5',
    'PSTM': '1681464020',
    'MCITY': '-288%3A',
    'ZFY': 'fvcLnKxkNtz8igyv1qho6yPgLbe9qGpS0m32NwlZL6s:C',
    'BAIDU_WISE_UID': 'wapp_1688263766258_411',
    'APPGUIDE_10_6_2': '1',
    'APPGUIDE_10_6_5': '1',
    'APPGUIDE_10_6_6': '1',
    'BAIDUID': '4F8251AFEB423D30EEA1DB5E23BC7415:FG=1',
    'BAIDUID_BFESS': '4F8251AFEB423D30EEA1DB5E23BC7415:FG=1',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1698732412',
    'APPGUIDE_10_6_7': '1',
    'ab_sr': '1.0.1_YjMwNWNkN2RmYjVhYmY2NzdiYWEwMzBmNTdkNTNkYmFiZjZlMDkyMGRiMGYzODczMmJlYmNhNWRmOTUxMTVjOTIxMDY1ZTNmMDk5NWU0MjBmNTQzOGU3NTczMDRmM2E1NGRkMWVhNzNiNWJlOWFiMGNhMWViMDhlNjczMWY0MjE4MDE1ZGVlZDE1NTM0ZjlmMWZkZWExODhmYTExZGU0Mg==',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Acs-Token': '1699607373040_1699607627476_r+5lTjTcgH/OE0PI0XElq6GOBrU1+HstQrMiw1/xrqsE4XRzVn/OHpPSKOFPBpR4WmGx87Ab1MgFPTvPrk5f9UKFTLBrnTnecwCvD5Wr5k7Cz0yEEV+4NmY93nCg7nnGQwpEU5rZRhMju+9K3t32S9JcDUL6tTqLQ4bKRK91eODwXV9ZQXl87zKUxK25SCDQwxXw3YVURxFh2O9I0yfct11hiaRAkDRtXECs1zBhCFIv4c6Dd/QgDm9Wv1jMGrydToixggjJTHh05awyQTjIU//aqNa+N207leH+vQvW6f/9zAq9Fp/SKAladh4rp9GFf7HbQAvsR2OI+/hWyY3xb78bI9aQ9QH03LX5kpB9MfvLwSlcpdIpQc3+/Np8hEep8jrITGc8TdtRb56/sPZUIKkKGpCqjzoWSxDYU8P4ne5utJg+omr11eQSBHUCKmT5kStpKSQTqljnFxgYKfecNsHEV7x05tnDge31SAludDyc8WkdOKMZye55TmV+iB5YpG6AI3qcEoQIQVF94yUrBQ==',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=CA328BEADA915A3A3036972318E84BA5; PSTM=1681464020; MCITY=-288%3A; ZFY=fvcLnKxkNtz8igyv1qho6yPgLbe9qGpS0m32NwlZL6s:C; BAIDU_WISE_UID=wapp_1688263766258_411; APPGUIDE_10_6_2=1; APPGUIDE_10_6_5=1; APPGUIDE_10_6_6=1; BAIDUID=4F8251AFEB423D30EEA1DB5E23BC7415:FG=1; BAIDUID_BFESS=4F8251AFEB423D30EEA1DB5E23BC7415:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1698732412; APPGUIDE_10_6_7=1; ab_sr=1.0.1_YjMwNWNkN2RmYjVhYmY2NzdiYWEwMzBmNTdkNTNkYmFiZjZlMDkyMGRiMGYzODczMmJlYmNhNWRmOTUxMTVjOTIxMDY1ZTNmMDk5NWU0MjBmNTQzOGU3NTczMDRmM2E1NGRkMWVhNzNiNWJlOWFiMGNhMWViMDhlNjczMWY0MjE4MDE1ZGVlZDE1NTM0ZjlmMWZkZWExODhmYTExZGU0Mg==',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'from': 'zh',
    'to': 'en',
}

data = {
    'from': 'zh',
    'to': 'en',
    'query': '睡觉',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': res['data'],
    'token': 'af7d8ce639d9127a008b49a2ac637315',
    'domain': 'common',
    'ts': int(time.time()*1000),
}

response = requests.post('https://fanyi.baidu.com/v2transapi', params=params, cookies=cookies, headers=headers, data=data).json()
print(response)
print(response['trans_result']['data'][0]['dst'])