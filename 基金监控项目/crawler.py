"""
爬虫文件
"""
import requests,re,json


def get_data(id:str):
  # 获取所有证券号
  res1 = requests.get('http://fund.eastmoney.com/js/fundcode_search.js?v=20220325212048')
  all_list = json.loads(re.findall('var r = (.*?);',res1.text)[0])
  try:
    title=''
    for i in all_list:
      if id == i[0]:
        title = i[2]
        break
    res = requests.get(f'https://danjuanfunds.com/djapi/fund/growth/{id}?day=1m',headers={'user-agent':'123121313'}).json()
    if res['result_code']==0:
      data:list = res['data']['fund_nav_growth']
      date=[]
      value=[]
      for i in data:
        date.append(i['date'][5:])
        value.append(i['value'])
      return {'date':date, 'value':value,'title':title}
    else:
      return {'date':None, 'value':None,'title':title}
  except Exception as e:
    return {'date':None, 'value':None,'title':None}

# get_data()
