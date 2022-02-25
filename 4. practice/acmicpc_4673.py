# 셀프넘버 만들기

i=0
all_num = list(range(1,10000+1))
no_self=[]
for i in range(1,10000):
    k2=0
    k3=0
    for value in enumerate(str(i)):
        k1 = list(value)[1]
        k2 += int(k1)
    k3 = i+k2
    no_self.append(k3)
self_num =list(set(all_num)-set(no_self))
self_num.sort()
for i in range(len(self_num)):
    print(self_num[i])
