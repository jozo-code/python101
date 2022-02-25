# append 함수를 이용하면 마지막 인덱스에 아이템을 추가할 수 있다.

students =['홍길동','박찬호','이용규','박승철','김지은']
students.append("강호동")
print(students)


# 묶음을 추가할 수도 있음

myFamilyAge =[['아빠',40],['엄마',40],['나',10]]
myFamilyAge.append(['동생',5])
print(myFamilyAge)


# insert 함수를 이용하면 특정 위치에 아이템을 추가할 수 있다.

students.insert(2,"조효진") # 2번에 조효진 학생을 추가하면 찬호부터 밀림
print(students)


# 오름차순이 유지되도록 숫자 끼워넣기

numbers = [1,3,5,11,45,54,62,74,85]
inputNumber = int(input('숫자입력:'))
insertIdx = 0

for idx, number in enumerate(numbers):
    print(idx, number)
    if insertIdx==0 and inputNumber < number:
        insertIdx = idx
numbers.insert(insertIdx,inputNumber)
print(numbers)