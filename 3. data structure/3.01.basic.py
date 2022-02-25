# 여러개의 데이터가 묶여 있는 자료형을 컨테이너 자료형이라고 함
# 컨테이너 자료형의 데이터 구조를 자료구조라고 함

# 자료구조 : 리스트, 튜플, 딕셔너리, 셋트
 ## 리스트는 자료 교체 가능, 튜플은 안됨, 딕셔너리는 키 값에 해당하는 밸류 값이 있는 데이터, 셋트는 중복된 데이터 허용하지 않음

student1 ="홍길동"
student2 ="박찬호"
student3 ="이용규"
student4 ="박승철"
student5 ="김지은"

students = ["홍길동","박찬호","이용규","박승철","김지은"] #리스트
print(student1) # 변수 출력
print(students) # 리스트 출력
print(type(students)) # 자료형 출력

# for 문을 이용할 때는 이렇게 # 리스트에 담긴 학생이름이 순차적으로 출력됨
for student in students:
    print(students)



students_t = ("홍길동","박찬호","이용규","박승철","김지은") #튜플

scores_dic = {"kor":95,"eng":80,"mat":100} #딕셔너리

allSales = {100,200,200,500} #셋트
print(allSales) # 중복을 허용하지 않으므로 200이 한 개만 나온다.
