# 등차수열의 합 구하기

inputN1=int(input("a1 입력:"))
inputD=int(input("공차 입력:"))
inputN=int(input("n 입력:"))

valueN=0
sumN=0
n=1

# an = a1 + (n-1)d
#sn = n(a1+an)/2

valueN = inputN1 + (inputN-1)*inputD
sumN = inputN * (inputN1 + valueN) / 2
print("{}번째 항까지의 값:{}".format(inputN, int(sumN)))
