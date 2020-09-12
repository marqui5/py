#!/usr/bin/env python
import math
import time
n = int(input('Please input range: '))
a = []
for i in range(n + 1):
    a.append(i)
a[1] = 0
rt = int(math.sqrt(n))
cnt = 0
start = time.time()
for i in range(2, rt + 1, 1):
    #cnt += 1
    for j in range(i * i, n + 1, i):
        #输出多少个零则有多少个数被重复筛选，需要进一步优化，保证每个数只被筛选一次
        #print(a[j])
        a[j] = 0
        #cnt += 1
stop = time.time()
print("----------split line----------")
print(list(filter(lambda x:x > 0,a)))
print("calc times: " + str(cnt))
print("duration: " + str((stop-start)*1000))
