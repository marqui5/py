#!/usr/bin/env python
import time
start = time.time()
print(list(filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), range(2, int(input('Please input a range of prime: '))))))
stop = time.time()
print("duration: " + str((stop-start)*1000))
