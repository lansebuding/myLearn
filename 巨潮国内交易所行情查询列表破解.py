import requests
import execjs

cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1698379746',
    'MALLSSID': '4937596C7A594C6F473645386A655149424D364C656A54766C49584F544F384A52575847425A444749612F486D676F4136683072696E4F6D744C54512F2F706A',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1698379766',
}

code = open('./混淆.js','r',encoding='utf-8').read()
pwd = execjs.compile(code).call('getResCode')

print(pwd)
headers = {
    'Accept': '*/*',
    'Accept-EncKey': pwd,
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1698379746; MALLSSID=4937596C7A594C6F473645386A655149424D364C656A54766C49584F544F384A52575847425A444749612F486D676F4136683072696E4F6D744C54512F2F706A; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1698379766',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'tdate': '2023-10-26',
    'market': 'SZE',
}

response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007', cookies=cookies, headers=headers, data=data).json()

print(response)