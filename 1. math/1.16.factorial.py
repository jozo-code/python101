# 파이썬을 이용해서 팩토리얼 결과값을 출력하는 프로그램 만들기

inputN=int(input("n 입력: "))

# result=1
# for n in range (1,(inputN+1)):
#     result *=n

# print("{}팩토리얼: {}".format(inputN,result))


# 함수도 쓸 수 있음

# def factorialFun(n):
#     if n==1: return 1
    
#     return n * factorialFun(n-1)


# print("{}팩토리얼: {}".format(inputN,factorialFun(inputN)))

# 라이브러리 호출해서 쓸 수도 있음
import math
print("{}팩토리얼: {}".format(inputN,math.factorial(inputN)))
