import requests

cookies = {
    'OUTFOX_SEARCH_USER_ID_NCOO': '2094177160.0451846',
    'OUTFOX_SEARCH_USER_ID': '688645544@113.128.240.98',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=2094177160.0451846; OUTFOX_SEARCH_USER_ID=688645544@113.128.240.98',
    'Pragma': 'no-cache',
    'Range': 'bytes=0-',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'audio',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'audio': 'have a meal',
    'type': '2',
}

response = requests.get('https://dict.youdao.com/dictvoice', params=params, cookies=cookies, headers=headers)

print(type(response.content))


with open('./1.mp3','wb') as file:
    file.write(response.content)