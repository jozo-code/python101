# 논리형 데이터를 사용해서 무한반복을 하거나 멈출 수 있다.


# flag를 이용해보자

flag=True
num=0
sum=0
while flag:
    num+=1
    sum+=num
    print(num, sum)

    if sum >= 1000:
        flag = False #if를 만족한 경우 반복문이 false가 되면서 멈춘다.


#---------------------------------------------------------
 # 예제 환자가 하루 50~100명 올 때 누적 환자 10000명이 넘는 날짜 구하기

import random

sum=0
date=1
flag=True

while flag:
    patientCount = random.randint(50,100)
    sum += patientCount
    date += 1
    print("날짜:{} \t 오늘환자수:{}, \t 누적환자수:{}".format(date, patientCount,sum))    
    if sum>= 10000: # 합이 만이 넘을 때 반복문 종료
        flag = False