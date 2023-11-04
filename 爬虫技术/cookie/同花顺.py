"""
主要是cookie反爬
使用hook找到发送请求位置
再顺着堆栈往上走
发现它的生成逻辑用到了许多全局变量
将整个js复制下来----------注意不一定是js生成的，要看是否是后台返回的cookie
外部定义一个变量，放到局部作用域，赋值函数，外层调用
发现缺环境，使用jsdom进行补充
成功模拟
替换自己模拟的参数
请求成功


"""


import requests
import execjs
code = open('./爬虫技术/cookie/cookie.js','r',encoding='utf8').read()
_v = execjs.compile(code).call('TEXTS')
print(_v)
cookies = {
    'Hm_lvt_722143063e4892925903024537075d0d': '1699064855',
    'log': '',
    'Hm_lvt_929f8b362150b1f77b477230541dbbc2': '1699064856',
    'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1': '1699064856',
    'Hm_lpvt_722143063e4892925903024537075d0d': '1699064862',
    'Hm_lpvt_929f8b362150b1f77b477230541dbbc2': '1699064863',
    'Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1': '1699064863',
    'v': _v,
}

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_722143063e4892925903024537075d0d=1699064855; log=; Hm_lvt_929f8b362150b1f77b477230541dbbc2=1699064856; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1699064856; Hm_lpvt_722143063e4892925903024537075d0d=1699064862; Hm_lpvt_929f8b362150b1f77b477230541dbbc2=1699064863; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1699064863; v=A7NmajFC0h9duZ7L5SDOPQA5QrzY6EauAX6L22VQDREIut2i7bjX-hFMGxB2',
    'Pragma': 'no-cache',
    'Referer': 'https://q.10jqka.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'hexin-v': _v,
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/3/ajax/1/',
    cookies=cookies,
    headers=headers,
)

print(response.text)