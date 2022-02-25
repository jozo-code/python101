#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

n = int(input())
N = list(map(int, input().split())) # 리스트로 숫자 입력

minScore = 0; maxScore=0
minScoreIdx = 0; maxScoreIdx = 0

for idx, score in enumerate(N):
    if idx==0 or minScore>score: # 처음에 0일 때 값 할당 후에 idx는 0은 아니지만 조건에 만족하는 경우 최저점과 최저점인덱스 갱신
        minScoreIdx = idx
        minScore=score

for idx, score in enumerate(N):
    if maxScore<score: # 처음에 0일 때 값 할당 후에 idx는 0은 아니지만 조건에 만족하는 경우 최저점과 최저점인덱스 갱신
        maxScoreIdx = idx
        maxScore=score
print(N[minScoreIdx],N[maxScoreIdx]) # 인덱스 찾았으니 최고점 최저점 없애기
