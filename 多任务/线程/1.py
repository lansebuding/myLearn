"""
同时进行

线程特点：
1.随机执行
  线程是操作系统分配的最小执行单位---它不受python解释器控制
  名词---时间片轮训
  本质是在同一时间内多个任务来回执行并快速切换，看起来就是同时执行
  它是假多线程，GIL

"""
import time
import threading # 让程序成为多任务程序--多线程


def sing(k):
  for i in range(3):
    print('sing')
    print(k)
    # time.sleep(1)

def dance():
  for i in range(3):
    print('dance')
    # time.sleep(1)

def main():
  t1 = threading.Thread(target=sing,args=('你好',)) # 线程对象1
  t2 = threading.Thread(target=dance) # 线程对象2
  t1.start() # 子线程1
  # time.sleep(1) #干扰执行顺序
  t2.start() # 子线程2
  # time.sleep(1)
  print(len(threading.enumerate()))

if __name__ == '__main__':
  main() # 主线程


