#첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
#둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.


n,x=map(int, input().split())
A = list(map(int, input().split())) # 리스트로 숫자 입력

for i in range(n):
    if A[i]<x: # 리스트의 i번째 숫자랑 x 비교
        print(A[i], end=" ") # 조건 만족하는 숫자 출력