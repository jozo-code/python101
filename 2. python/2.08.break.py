# break로 무한 반복문 빠져나오기

num=0

while True:
    print("hello")
    num +=1
    if num >=5:
        break
print("end")

# 예제

# 2.2kg이 넘으면 강아지 이유식 중단, 한번 이유식 먹을 때 70g 증가, 예상되는 이유식 중단 날짜는? (현재는 800g)

limitWeight=2200
currntWeight=800
date=1

while True:
    if currntWeight>=2200:
        break
    date+=1
    currntWeight+=70
print("이유식 중단:{}일".format(date))