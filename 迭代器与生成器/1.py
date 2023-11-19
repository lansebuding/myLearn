arr = [1,2,3]

obj = arr.__iter__()

# 内置__iter__方法的对象就是迭代器对象
# print(arr.__iter__())

# for i in obj:
#   a1 = i+1
#   b1 = i+2
#   print(i)

"""
可迭代对象：内置__iter__方法

迭代器：内置__iter__ , __next__方法

for本质：
对传入的数据进行__iter__得到一个迭代器，再一直调用__next__方法，直到抛出异常break
"""

"""
生成器是自定义的迭代器
和for循环配套使用
"""

def test():
  print('Testing1')
  # 代码不执行，返回一个生成器对象
  yield
  print('Testing2')
  yield

# my_iter=test()
# print(my_iter is my_iter.__iter__())
# print(my_iter.__next__())
# print(my_iter.__next__())
# my_iter.__next__()
# my_iter.__next__()

# for i in my_iter:
#   # print(i)
#   pass

# 生成器生成斐波那契数列
def r(n):
  i,a,b=0,1,1
  while i<n:
    yield a
    a,b = b,a+b
    i+=1

# 生成器模拟range
def my_range(a,b=0):
  while b<a:
    yield b
    b+=1

# 生成器计算阶乘
def jie(n):
  i,j=1,1
  while i<=n:
    yield j
    i+=1
    j=i*j

# for i in jie(10):
#   print(i)

# print(sum(list(jie(10))))

from hashlib import new
import random,time
# def fn(func:'function',a:int,b:int):
#   return func(a,b)

# print(fn(lambda a,b:a+b,100,200))

# aaa={
#   'YJW':111,
#   'YJW2':222,
#   'YJW3':50,
#   'YJW4':-555
# }

# print(max(aaa,key=lambda a:aaa[a]))
# print(aaa[max(aaa,key=lambda a:aaa[a])])

# list1 = [1,4,6,-1,-88,50]

# print(sorted(list1,reverse=True))


"""
装饰器是一个特殊的闭包
"""

def run(x:int):
  print('out')
  def inner():
    print(x+4000)
  return inner

# 装饰器
def decrease(func:'function'):
  def new_test(a:int):
    print('=======')
    func(a)
    print('=========')
  return new_test

# 装饰器
@decrease
def test(a:int):
  print(a+4)
# test=decrease(test)

# test(2)


def dess(func:'function'):
  def new_de():
    start = time.localtime()
    # print(f'开始时间：{start}')
    func()
    end = time.localtime()
    # print(f'结束时间：{end}')
  return new_de



@dess
def test_time():
  for i in range(1000000):
    pass
  print('done')


test_time()