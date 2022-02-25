# while을 이용한 list 아이템 조회하기

cars=['그랜저','소나타','말리부','카니발','쏘렌토']

# 방법1
n=0
while n < len(cars):
    print(cars[n])
    n+=1

# 방법2
n=0
while True:
    print(cars[n])
    n+=1
    if n == len(cars):
        break


## 학급별 학생수, 전체학생수, 평균학생수 출력하기
studentCnts = [[1,18],[2,19],[3,18],[4,18],[5,18],[6,18],[7,17]]

n=0
sum=0
avg=0
while n < len(studentCnts):
    classNo = studentCnts[n][0]
    cnt = studentCnts[n][1]
    print("{}학급 학생수:{}명".format(classNo,cnt))

    sum += cnt
    n +=1

print("전체 학생 수 :{}명".format(sum))
print("평균 학생 수 :{}명".format(sum/len(studentCnts)))


