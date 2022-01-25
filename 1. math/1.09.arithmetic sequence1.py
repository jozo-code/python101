# 다음 수열을 보고 n번째 항의 값을 출력하는 프로그램을 만들어보자. an ={2,5,8,11,14,....}

inputN1=int(input("a1 입력:"))
inputD=int(input("공차 입력:"))
inputN=int(input("n 입력:"))

valueN=0
n=1

# while n <= inputN:
#     if n ==1:
#         valueN=inputN1
#         print("{}번째 항의 값:{}".format(n, valueN))
#         n += 1
#         continue

#     valueN = valueN + inputD
#     print("{}번째 항의 값: {}" .format(n, valueN))
#     n +=1

# print("{}번쨰 항의 값:{}".format(inputN, valueN))


# 이렇게 쉽게도 쓸 수 있음

valueN = inputN1 + (inputN-1) * inputD
print("{}번째 항의 값: {}".format(inputN,valueN))

