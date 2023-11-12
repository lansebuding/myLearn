"""
一个程序运行后，用到的资源就是进程

进程是操作系统分配资源的基本单位

特点：
1.进程开启后，至少有一个线程
2.进程和线程都可以完成多任务
3.进程创建的消耗时间比线程大很多（因为要分配cpu，内存等资源）
4.开启时操作系统会分配一个进程id
5.多进程之间不共享全局变量

适用场景
进程：密集型运算场景
线程：IO网络任务场景
"""

import time,threading

import multiprocessing

# 获取进程pid
import os

def test1():
  for i in range(5):
    print(f'in test1 i={i}')
    time.sleep(.5)
  print(f'in test1 pid={os.getpid()}, ppid = {os.getppid()}')
def test2():
  for i in range(5):
    print(f'in test2 i={i}')
    time.sleep(.5)
  print(f'in test2 pid={os.getpid()}, ppid = {os.getppid()}')
def main():
  # t1 = threading.Thread(target=test1)
  # t2 = threading.Thread(target=test2)
  t1=multiprocessing.Process(target=test1)
  t2=multiprocessing.Process(target=test2)
  t1.start()
  t2.start()

if __name__ == "__main__":
  main()