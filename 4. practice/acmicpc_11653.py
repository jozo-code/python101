#백준 11653번 소인수분해 문제

N = int(input("1보다 큰 정수 입력: "))
m = 2 
while N!=1:
    if N%m==0: 
        print(m) 
        N = N//m 
    else: m += 1

