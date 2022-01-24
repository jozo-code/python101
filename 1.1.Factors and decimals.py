# 파이썬을 이용해서 사용자가 입력한 숫자의 약수를 출력해보자

inputNumber = int(input("0보다 큰 정수 입력: "))


for number in range(1, inputNumber+1) :
    if inputNumber % number == 0:
        print("{}의 약수: {}".format(inputNumber,number))