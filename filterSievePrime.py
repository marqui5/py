import time
cnt = 0
def _odd_iter():
     n = 1
     while True:
         n = n + 2
         yield n
def _not_divisible(n):
     return lambda x: x % n > 0
def primes():
     yield 2
     it = _odd_iter() # 初始序列
     while True:
         n = next(it) # 返回序列的第一个数
         yield n
         it = filter(_not_divisible(n), it) # 构造新序列
i = int(input('Please input a range of prime: '))
start = time.time()
for n in primes():
    if n < i:
        #print(n)
        pass
    else:
        print(n)
        break
stop = time.time()
print("calc times: " + str(cnt))
print("duration: " + str((stop-start)*1000))
