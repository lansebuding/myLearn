from email import header
import requests
import pprint

# params = {
#   'group':'tt-test2',
#   'action':'toutiao',
#   'url':'https://www.toutiao.com/search/suggest/hot_words/'
# }
# # https://www.toutiao.com/search/suggest/hot_words/?_signature=_02B4Z6wo00f01Lyp4ogAAIDBlyO5Tlsa2ES8jeYAAEpnf4
# res = requests.post('http://127.0.0.1:5612/business-demo/invoke',data=params).json()

# pprint.pprint(res)
seccsion = requests.session()
def get_url(url:str):
  params = {
    'group':'tt-test2',
    'action':'toutiao',
    'url':url
  }
  res = requests.get('http://127.0.0.1:5612/business-demo/invoke',params=params).json()
  if('?' in url):
    url+='&_signature={}'.format(res['signature'])
  else:
    url+='?_signature={}'.format(res['signature'])
  return url,res['cookie']


def get_data(url:str,cookies):
  headers = {
      'authority': 'www.toutiao.com',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cookie': cookies,
      'referer': 'https://www.toutiao.com/?wid=1699271316386',
      'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
  }
  res = seccsion.get(url,headers=headers).json()
  pprint.pprint(res)

url1,cookies = get_url('https://www.toutiao.com/api/pc/list/feed?channel_id=0&max_behot_time=1699278609&offset=0&category=pc_profile_recommend&aid=24&app_name=toutiao_web')
print(url1)
# _02B4Z6wo00f01i5Xu4gAAIDDBd3gTC2P5n4uc78AAO7r30
# get_data(url1,cookies)


