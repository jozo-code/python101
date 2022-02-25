# 피보나치 수열은 an = an-2 + an-1


inputN = int(input())
valuePreN2 = 0
valuePreN1 = 0

n=1
while n <= inputN:
    if n  == 1 or n==2:
        valueN =1
        valuePreN2 = valueN
        valuePreN1 = valueN
        n +=1
    
    else:
        valueN=valuePreN2+valuePreN1
        valuePreN2=valuePreN1
        valuePreN1=valueN
        n +=1
print(valueN)


