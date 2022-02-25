#첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.


# C = int(input())
# for i in range(C): 
#     N = list(map(int, input().split(" ")))
#     up =[]
#     avg = sum(N[1:])/N[0]
#     #print(avg)
#     for j in range(1,len(N)):
#         if N[j] > avg:
#             print(N[j])
#             up.append(N[j])
#     #print(len(up))
#     #print(N[0])
#     value = len(up)/N[0]
#     print("{:3.3%}".format(value))

N_N = [[2,3,3,3], [23,3,3,]]
    
C = int(input())
N_N = []
for i in range(C): 
    N = list(map(int, input().split(" ")))
    N_N.append(N)
for i in range(C): 
    N = N_N[i]
    up =[]
    avg = sum(N[1:])/N[0]
    # print(avg)
    for j in range(1,len(N)):
        if N[j] > avg:
            # print(N[j])
            up.append(N[j])
    # print(len(up))
    # print(N[0])
    value = len(up)/N[0]
    print("{:3.3%}".format(value))