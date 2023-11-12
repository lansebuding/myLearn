import multiprocessing
from queue import Queue

def down(q:Queue):
  arr = [1,2,3,4]
  for i in arr:
    q.put(i)
  print('数据存入队列完毕')


def deal(q:Queue):
  my_arr = []
  while True:
    my_arr.append(q.get())
    if q.empty():
      break
  print(my_arr)

def main():
  q = multiprocessing.Queue()
  t1 = multiprocessing.Process(target=down,args=(q,))
  t2 = multiprocessing.Process(target=deal,args=(q,))
  t1.start()
  t2.start()

if __name__ == '__main__':
  main()