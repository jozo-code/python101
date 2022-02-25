# 값을 출력할 때 print() 함수를 이용

userName = "홍길동"
print(userName)

# 콤마를 쓰면 데이터 연속 출력 가능

print("User name : ", userName)

# print를 연달아쓰면 자동으로 엔터가 들어간 것처럼 출력되는데 end=""를 입력해서 연달아 출력하게 할 수 있음

print("3*5=",end="")
print(3*5)

print("3*5=")
print(3*5)

# format을 이용할 수 있음

print(f'User name : {userName}') # 변수명은 중괄호 안에다가 넣는다.

# 탭(듸어쓰기 4개)을 넣거나 엔터(계행)를 넣을 수 있음
print(f'User name\t :\t \n{userName}') # 탭은 \t 이고 계행은 \n