
import base64
import json
import time,datetime,hashlib
class Test:

  name='YJW'
  age=25
  sex='男'

  def __init__(self,score):
    self.score=score
    pass
  
  # 自动执行，销毁对象，GC垃圾回收
  def __del__(self):
    print('--')
  
  def sing(self):
    print('Father')

class Child(Test):
  def __init__(self,score):
    # self.name=name
    super().__init__(score)
    # self.score=score
  def sing(self):
      print(self.score)



# Child(100).sing()
# Test(100).sing()


print(time.strftime("%Y-%m-%d %H:%M:%S"))

now_tiem = datetime.datetime.now()
print(now_tiem.month)

#加三天
print((datetime.datetime.now()+datetime.timedelta(3)).strftime("%Y-%m-%d %H:%M:%S"))

a = hashlib.md5()

a.update('hello'.encode('utf8'))
print(a.hexdigest())

# base64

a1 = base64.b64encode('你好'.encode('utf8'))
print(a1)
print(base64.b64decode(a1).decode('utf8'))

my_dic = {
  'name':'英语',
  'age':20
}

# with open('./1111111.json','w',encoding='utf8') as f:
#   json.dump(my_dic,f,ensure_ascii=False)