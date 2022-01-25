# 유클리드 호제법 : x,y의 최대공약수는 y, r(x%y)의 최대공약수와 같다. 여기서 r은 x를 y로 나눴을 때의 나머지
# 유클리드 호제법을 이용해서 최대공약수 구하기

num1 = int(input("1보다 큰 정수 입력: "))
num2 = int(input("1보다 큰 정수 입력: "))

temp1 = num1
temp2 = num2

while temp2 > 0:
    temp = temp2
    temp2 = temp1 % temp2 #temp2는 temp1을 temp2로 나눈 나머지
    temp1 = temp

print('{}, {}의 최대공약수: {}'.format(num1, num2, temp1))
