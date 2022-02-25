# 피보나치 수열은 an = an-2 + an-1

from more_itertools import value_chain


inputN = int(input("n 입력: "))

valueN = 0
sumN = 0

valuePreN2 = 0
valuePreN1 = 0

n=1
while n <= inputN:
    if n  == 1 or n==2:
        valueN =1
        valuePreN2 = valueN
        valuePreN1 = valueN

        sumN += valueN
        n +=1
    
    else:
        valueN=valuePreN2+valuePreN1
        valuePreN2=valuePreN1
        valuePreN1=valueN
        sumN+=valueN
        n+=1
print("{}번쨰 항의 값: {}".format(inputN, valueN))
print("{}번쨰 항까지의 값: {}".format(inputN, sumN))