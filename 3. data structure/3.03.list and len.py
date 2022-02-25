# 리스트의 길이란 리스트에 저장된 아이템의 개수를 말한다.

students = ['홍길동','박찬호','이용규','박승철','김지은']
print(len(students))


# for과 len을 함께 이용하기

for i in range(len(students)):
    print(students[i])


# 그냥 이렇게 써도 됨

for i in students:
    print(i)