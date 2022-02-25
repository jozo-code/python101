# pop으로 원하는 아이템을 삭제할 수 있음

students =['홍길동','박찬호','이용규','박승철','김지은']
students.pop() #마지막 데이터 삭제
print(students)
rValue = students.pop(2) #2번 데이터 삭제하고 삭제된 데이터 담기
print(students)
print(rValue) 


# 체조선수의 최저 최고 점수를 찾아서 빼기

playerScores = [9.5, 8.9, 9.8, 9.8, 8.8, 9.0]
print(playerScores)

minScore = 0; maxScore=0
minScoreIdx = 0; maxScoreIdx = 0

for idx, score in enumerate(playerScores):
    if idx==0 or minScore>score: # 처음에 0일 때 값 할당 후에 idx는 0은 아니지만 조건에 만족하는 경우 최저점과 최저점인덱스 갱신
        minScoreIdx = idx
        minScore=score
playerScores.pop(minScoreIdx)

for idx, score in enumerate(playerScores):
    if maxScore<score: # 처음에 0일 때 값 할당 후에 idx는 0은 아니지만 조건에 만족하는 경우 최저점과 최저점인덱스 갱신
        maxScoreIdx = idx
        maxScore=score
print(minScoreIdx,maxScoreIdx, end=" ") # 인덱스 찾았으니 최고점 최저점 없애기

playerScores.pop(maxScoreIdx)
print(playerScores)