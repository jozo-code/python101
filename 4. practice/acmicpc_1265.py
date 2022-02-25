# 1부터 N까지의 수를 임의로 배열한 순열은 총 N! = N×(N-1)×…×2×1 가지가 있다.
# 모든 1 ≤ i ≤ N에 대해서 |P[i] - i| ≤ K를 만족하는 순열 P의 개수를 구하는 프로그램을 작성하시오.


# 1부터 N까지의 수를 임의로 배열한 순열
# 1부터 N 사이의 i를 이용해 순열의 개수-i를 계산하고, K와 같거나 작은 순열 P의 개수를 구해라


# # N과 K를 입력
import math

N, K = map(int, input().split())
p_cnt=0
# i는 1부터 N사이의 수
for i in range(1,N+1):
    p=math.factorial(i)
    if p-i <= K:
        p_cnt +=p
print(p_cnt)


# # list에 1!~n!까지 순서대로 넣기

# import math
# n, K = map(int, input().split())

# pacto_list =[]
# for i in range(1,n+1):
#     pacto = math.factorial(i)
#     if pacto - i <=K:
#         pacto_list.append(pacto)
# print(sum(pacto_list))

