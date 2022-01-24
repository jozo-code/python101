inputNumber = int(input("0보다 큰 정수 입력: "))


for number in range(2,inputNumber+1):
    flag = True

    for n in range(2, number):
        if number % n == 0:
            flag = False
            break #소수의 대상이 아니기 때문에 끊어버림

    if flag:
        print("{} : 소수".format(number))
    else:
        print("{} : 합성수".format(number))
