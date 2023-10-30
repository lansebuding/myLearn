import json
import csv
import pymysql
# 写入xlsx
from openpyxl import Workbook
from elasticsearch import Elasticsearch

data = [{'name':'杨佳伟','age':25},{'name':'yjw2','age':23}]

# json文件
# with open('./ccc.json','w',encoding='utf8') as file:
#   file.write(json.dumps(data,ensure_ascii=False))


# csv文件
# with open('./ccc.csv','w',encoding='utf8') as file:
#   cs = csv.writer(file)
#   cs.writerow(['id','name','age'])
#   cs.writerow(['01','YJW',25])
#   cs.writerow(['02','杨佳伟',25])
#   cs.writerows([['01','YJW',25],['02','杨佳伟',25]])

# xlsx文件
# wb = Workbook()
# ws = wb.create_sheet('s1',0)
# ws.append(['姓名','年龄'])

# ws.append(['YJW',25])
# ws.append(['杨佳伟',25])

# wb.save('./ddd.xlsx')

# 连接数据库
data1 = [{'id':'2','name':'杨佳伟','age':25},{'id':'3','name':'yjw2','age':23}]


def test(datas):
  conn = pymysql.connect(host='localhost',port=3306,password='a1846770113',user='root',database='text')
  cursor = conn.cursor()

  # cursor.execute('SELECT * FROM tt')

  # res = cursor.fetchall()
  sql = 'insert into tt (id,name,age) values (%s , %s, %s)'
  # datas = ('1','YJW',25)
  try:
    cursor.execute(sql,datas)
    conn.commit()
  except:
    conn.rollback()
    print('失败')

  cursor.close()
  conn.close()

def deal_data(data):
  for row in data:
    tu = (row['id'],row['name'],row['age'])
    test(tu)

# deal_data(data1)

es = Elasticsearch('https://localhost:9200', verify_certs=False)

result = es.indices.create(index='YJW',ignore = 400)

print(result)