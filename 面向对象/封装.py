

class Test:
  
  # 前面加两个__就是封装，内部可访问
  __x=400
  y=100

  def getInfo(self):
    return self.__x

  # 前面加两个__就是封装，内部可访问
  def __gg(self):
    print('封装方法')

print(Test().getInfo())
obj = Test()
# 判断对象是否有指定属性
print(hasattr(obj,'y'))
if hasattr(obj,'y'):
  setattr(obj,'y',0)
  print(obj.y)

if hasattr(obj,'z') == False:
  setattr(obj,'z','hhh')
  print(obj.z)

if hasattr(obj,'getInfo'):
  m = getattr(obj,'getInfo')
  print(m)
  print(m())