#!/usr/bin/env python
n = int(input('Please input range: '))
a = []
p = []
#初始化两个长度为n的数组填入0表示都是素数
for i in range(n + 1):
    a.append(0)
    p.append(0)
cnt = 0
j = 1
#遍历2到n
for i in range(2, n + 1, 1):
    cnt += 1
    #如果a[i]=0则a[i]是素数，
    if(a[i] < 1):
    #p[0]+1纪录素数， p[0] 相当于 cnt，用来计数
    #把i赋值给p[1]，第一轮p[0]=1，p[1]=2
        p[0] += 1
        p[p[0]] = i
        print("p[0]="+str(p[0]))
        print("p[p[0]]="+str(p[p[0]]))
    #当j小于等于已记录的素数个数且i平方小于n，j加1，也就是遍历筛选素数的所有倍数
    while(j <= p[0] & (i * p[j] <= n)):
        print("j="+str(j)+" p[0]="+str(p[0])+" p[j]="+str(p[j])+" in")
        cnt += 1
        #素数p[j]的倍数都不是素数，标记为1
        a[i * p[j]] = 1
        #如果i除以最小的素数p[j]余数为零立刻退出筛选循环
        if(i % p[j] == 0):
            print("j="+str(j)+" p[0]="+str(p[0])+" p[j]="+str(p[j])+" out")
            break
    j += 1
    print("j= "+str(j))
print("----------split line----------")
print(list(filter(lambda x:x > 0,p)))
print("calc times: " + str(cnt))
