import math
import time
n = int(input('Please input range: '))
a = []
for i in range(n + 1):
    a.append(i)
a[1] = 0
cnt = 0
start = time.time()
for i in range(0, n + 1, 1):
    cnt += 1
    for j in range(2,int( math.sqrt(i)) + 1, 1):
        cnt += 1
        if(i % j == 0):
            a[i] = 0
stop = time.time()
print("----------split line----------")
print(list(filter(lambda x:x > 0,a)))
print("calc times: " + str(cnt))
print("duration: " + str((stop-start)*1000))
