import datetime
import time

d1 = {'name':'111','address':{'province':'370000'}}
d2 = {'age':20}
cont = {**d2,**d1} # 解包的形式合并字典
print(cont)

print(datetime.date(2023,11,4))
print(datetime.time(16,40,1))
print(int(round(time.time()*1000)))

print(time.localtime(1699087686.895).tm_year)