"""
主要是analysis参数破解
全局搜索analysis发现没有符合要求的参数，猜测该参数是拼接而成
使用hook找到请求位置
查询堆栈该参数出现位置，一步步跟进，找到生成位置
发现使用部分混淆
扣出js代码并还原
模拟生成该参数并替换
请求成功

注意模拟该请求传入参数值要和params参数名称对应


"""


import requests
import execjs
code = open('./爬虫技术/cookie/七麦.js','r',encoding='utf8').read()
# ['all','free','paid','grossing']
# ['iphone','ipad']
# ['cn','us']
t1 = input('输入榜单类型：')
t2 = input('输入设备类型：')
t3 = input('输入地区：')
# t4 = input('输入日期：')
# t5 = input('输入分页：')
arr = [t1, t2, t3, "36"]
analysis = execjs.compile(code).call('main',arr)
print(analysis)

headers = {
    'authority': 'api.qimai.cn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=omjs3k5v346saeq3ddje85l6e4; qm_check=A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWCwycRd1QlhAXFEGFUdASAFKBQcCCXsEBRFFIg4aHRoOBnMDARlGR2dQOVdICAolAGgCHBl0B3xUV05KVFsZXVJRWxsKFghJVktYVElWBRVP; gr_user_id=1da01ca5-900c-4cff-a017-0e1c77bf000c; ada35577182650f1_gr_session_id=94dad51d-361d-47ee-808b-b700cee54b48; ada35577182650f1_gr_session_id_sent_vst=94dad51d-361d-47ee-808b-b700cee54b48; synct=1699083433.916; syncd=-481',
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

params = {
    'analysis': analysis,
    'brand': t1,
    'device': t2,
    'country': t3,
    'genre': '36',
}

response = requests.get('https://api.qimai.cn/rank/index', params=params, headers=headers).json()

print(response)