# 사용자에게 데이터를 입력하도록 하는 input 함수
print("키보드를 통해서 데이터를 입력하세요.")
userInputData = input()
print(userInputData)

# 이렇게도 쓸 수 있음
userInputData = input("키보드를 통해서 데이터를 입력하세요.")
print(userInputData)

# 자료형을 지정해서 인풋 받을 수도 있음. 기본값은 문자형임.
userInputData = int(input("정수형을 입력하세요."))
print(userInputData)