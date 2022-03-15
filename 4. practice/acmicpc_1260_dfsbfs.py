# 입력 변수 받기
# N은 정점의 개수, M은 간선의 개수, V는 탐색을 시작할 정점의 번호, 각각의 라인에 간선이 연결하는 두 정점의 번호가 주어짐
N, M, V = map(int, input().split())

# 영행렬 생성
edge=[[0] * (N + 1) for i in range(N + 1)]

# 라인 체크
check = [0] * (N + 1)

# 라인에 1 입력
for i in range(M):
    a, b = map(int, input().split())
    edge[a][b] = edge[b][a] = 1

# 깊이 우선 탐색은 스택과 재귀함수를 이용한다.
def dfs(V):
    # 들어간 곳에 1 넣기
    check[V] = 1
    print(V, end=' ')
    # 재귀 함수 사용 V와 연결된 곳을 찾아서 함수 실행)
    for i in range(1,N+1):
        if(check[i]==0 and edge[V][i]==1):
            dfs(i)

# 너비 우선 탐색은 큐를 이용한다.            
def bfs(V):
    queue = [V]
    
    # dfs 끝났을 때 1로 모두 바뀌어있으니까 0으로 방문 체크
    check[V] = 0
    
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N + 1):
            if(check[i] == 1 and edge[V][i] == 1):
                queue.append(i)
                check[i] = 0
dfs(V)
print()
bfs(V)