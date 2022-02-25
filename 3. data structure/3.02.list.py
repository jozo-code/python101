# 리스트 선언하기

myFamilyNames =['홍아빠','홍엄마','홍길동','홍동생']
print(myFamilyNames)

todaySchedule = ['10시-업무회의','12시-친구와점심약속', '3시-자료정리','6시-운동','9시-TV시청']
print(todaySchedule)


# 인덱스는 아이템에 자동으로 부여되는 번호표, 파이썬은 무조건 0부터 시작한다.
# 리스트 아이템은 인덱스를 이용해서 조회할 수 있음

students = ["박찬호","홍길동","이용규","박승철","김지은"] #리스트
print(students(0))
print(students(1))
print(students(2))
print(students(3))
print(students(5)) # 5 없으니까 이렇게 쓰면 에러남


# for문을 이용해서 students 아이템 조회하기

students = ["김성예","신경도","박기준","최승철","황동석"] #리스트
for i in range(5):
    if i % 2 == 0:
        print("인덱스가 짝수인 경우 --> students[{}]:{}".format(i,students[i]))
    else:
        print("인덱스가 홀수인 경우 --> students[{}]:{}".format(i,students[i]))

