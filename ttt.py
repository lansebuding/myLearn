import hashlib
import time

# t = int(time.time()*1000)
t=1697510383902
x = hashlib.md5()
x.update(f'client=fanyideskweb&mysticTime={t}&product=webfanyi&key=EZAmCfVOH2CrBGMtPrtIPUzyv3bheLdk'.encode('utf-8'))

print(x.hexdigest())