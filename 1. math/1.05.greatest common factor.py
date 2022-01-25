# 두 개의 수를 입력하면 공약수와 최대공약수를 출력하는 코드를 작성하자.

num1 = int(input("1보다 큰 정수 입력: "))
num2 = int(input("1보다 큰 정수 입력: "))
maxNum =0

for i in range(1, (num1+1)):
    if num1 % i == 0 and num2 % i ==0 :
        print("공약수:{}".format(i))
        maxNum=i #mxNum에 계속 넣으면 어차피 계속 큰 수로 덮어쓰니까 최대공약수가 최종으로 남음

print("최대공약수:{}".format(maxNum))
