# 두수의 최소공배수 구하기
# num1이 num2 보다 작다고 가정하고 풀이
num1=int(input("1보다 큰 정수 입력: "))
num2=int(input("1보다 큰 정수 입력: "))
maxNum=0

for i in range(1, (num1+1)):
    if num1 % i == 0 and num2 % i == 0:
        print('공약수:{}'.format(i))
        maxNum=i #제일 끝에 최대공약수 i가 저장됨

print("최대공약수:{}".format(maxNum))

minNum = (num1 * num2) // maxNum # 두수를 곱하고 최대공약수를 나누면 그것이 최소공배수
print('최소공배수:{}'.format(minNum))
