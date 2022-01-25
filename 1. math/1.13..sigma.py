# 수식을 이용한 등차수열 합 구하기

# sn = n(a1+an)/2
# an = a1 + (n-1)d

inputN1=int(input("a1 입력:"))
inputD=int(input("공차 입력:"))
inputN=int(input("n 입력:"))

valueN=inputN1 + (inputN1-1)* inputD
sumN= inputN * (inputN1+valueN)/2

print("{}번째 항까지의 합:{}".format(inputN, int(sumN)))

# 수식을 이용한 등비수열 합 구하기
# sn = a1 * (1-r^n) / (1-r)


inputN1 = int(input("a1 입력: "))
inputR = int(input("공비 입력: "))
inputN = int(input("n 입력: "))

sumN = inputN1 * (1-(inputR ** inputN)) / (1-inputR)
print("{}번째 항까지의 합: {}".format(inputN,int(sumN)))