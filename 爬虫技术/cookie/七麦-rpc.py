import requests
import json
import re
from urllib import parse
import time,datetime


def get_localtime():
    return datetime.datetime.now().strftime('%Y-%m-%d')

baseURL = "https://api.qimai.cn"
path= "/rank/index"

dic = {'url':path,'params':{"brand": "paid", "device": "iphone", "country": "cn", "genre": "36","is_rank_index":'1',"page":'5',"date":get_localtime()},"baseURL": baseURL}


param = {"group": "t", "name": "test", "action": "fn", "param": json.dumps(dic)}

res = requests.get("http://127.0.0.1:12080/go", params=param).json()

analysis = re.findall(r'analysis=(.*?)$',json.loads(res['data'])['url'])[0]
analysis = parse.unquote(analysis)

dic1 = {
    'analysis':analysis,
    **dic['params']
}
print(dic1)
headers = {
    'authority': 'api.qimai.cn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'qm_check=A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWCwycRd1QlhAXFEGFUdASAFKBQcCCXsEBRFFIg4aHRoOBnMDARlGR2dQOVdICAolAGgCHBl0B3xUV05KVFsZXVJRWxsKFghJVktYVElWBRVP; gr_user_id=1da01ca5-900c-4cff-a017-0e1c77bf000c; PHPSESSID=nml7or12k1990lrqi5gud2gp9i; ada35577182650f1_gr_session_id=af5e39b7-a964-41cd-9cc3-523a1120aad7; ada35577182650f1_gr_session_id_sent_vst=af5e39b7-a964-41cd-9cc3-523a1120aad7; synct=1699343134.425; syncd=-1033',
    'origin': 'https://www.qimai.cn',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
res2 = requests.get(url=baseURL+path,params=dic1,headers=headers).json()
print(res2)