# 등비수열의 합


inputN1 = int(input("a1 입력: "))
inputR = int(input("공비 입력: "))
inputN = int(input("n 입력: "))

valueN = 0
sumN = 0
n=1

while n <= inputN:
    if n == 1:
        valueN=inputN1
        sumN+=valueN # 쭉 더해주는 것
        print("{}번째까지의 합: {}".format(n,sumN))
        n +=1
        continue
    valueN = valueN*inputR # valueN *= inputR 이라고 써도 됨
    sumN += valueN
    print("{}번쨰 항의 값: {}".format(n,valueN))
    n+=1


# 공식을 이용할 수도 있음
# sn = a1 * (1-r^n) / (1-r)
