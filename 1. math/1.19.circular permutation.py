# 원순열 공식 = (n-1)!
# 4명이 원탁 테이블에 앉을 수 있는 경우의 수를 계산하는 프로그램


n = int(input("사람 수 입력: "))
result=1
for i in range(1,n):
    result *= i
print("result:{}".format(result))
