import requests

def get_v():
  url = 'http://127.0.0.1:12080/go?group=t&name=test&action=get_v'
  response=requests.get(url=url).json()
  return response['data']

def get_data():
  _v = get_v()
  cookies = {
    'v': _v,
  }

  headers = {
      'Accept': 'text/html, */*; q=0.01',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
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
  return response.text


response = get_data()
print(response)