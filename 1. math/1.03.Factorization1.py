# 사용자가 입력한 수를 소인수분해

inputNumber = int(input("1보다 큰 정수 입력: "))

n=2
while n <= inputNumber:
    if inputNumber % n == 0:
        print("소인수:{}".format(n))
        inputNumber /= n
    else:
        n = n+1 #또는 n+=1 이라고 써도 됨

