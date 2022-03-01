import sys
input = sys.stdin.readline #라인별로 여러값을 입력 받고 싶을 때 사용하는 함수

n = int(input())
dp =[]
for i in range(n):
    dp.append(list(map(int,input().split()))) #계행없이 n줄로 여러값을 입력받도록 한다.
for i in range(1, len(dp)):
    dp[i][0] += min(dp[i-1][1],dp[i-1][2]) #i 번째 집을 1번 색으로 칠했을 때의 최소비용의 경우의 수는 i-1번째 집을 2번째, 3번째 색으로 칠했을 때의 최소비용에 i번째 집의 1번째 색 비용을 더한 값
    dp[i][1] += min(dp[i-1][0],dp[i-1][2])
    dp[i][2] += min(dp[i-1][0],dp[i-1][1])
print(min(dp[n-1]))
