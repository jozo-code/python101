# 학급별 학생 수 출력하기

studentsCnts = [[1,19],[2,20],[3,22],[4,18],[5,21]]

# len을 이용하면
for i in range(len(studentsCnts)):
    print("{}학급 학생수:{}".format(studentsCnts[i][0],studentsCnts[i][1]))

# 조금 더 간단하게
for i,k in studentsCnts:
    print("{}학급 학생수:{}".format(i,k))



# 과락 점수 출력

# 방법1
minScore = 60
scores =[['국어',58],['영어',77],['수학',89],['과학',99],['국사',50]]
for item in scores:
    if item[1] < minScore: #점수가 60보다 낮으면
        print("과락과목:{}, 점수:{}".format(item[0],item[1])) 
        
# 방법2
for subject, score in scores:
    if score < minScore: #점수가 60보다 낮으면
        print("과락과목:{}, 점수:{}".format(subject,score)) 


# 방법3 continue
for subject, score in scores:
    if score >= minScore: continue #점수가 60보다 높으면 컨티뉴로 패스
    print("과락과목:{}, 점수:{}".format(subject,score)) 
