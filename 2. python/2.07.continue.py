# 반복 실행 중 continue를 만나면 실행을 생략하고 다음 반복 실행문으로 넘어간다.
cnt=0
for i in range(1,100): #1부터 99까지
    if i%7 != 0 :#i가 7로 나눠지지 않으면
        continue # 다시 반복문으로 올라가세요
    print("{}는 7의 배수입니다.".format(i)) # 그럼 7의 배수만 출력되게 되는거임
    cnt+=1 #7의 배수 내려올 때마다 1씩 더해서 개수 세줌

else: # for문 다 끝나고 마지막에 따로 뽑고 싶은 게 있을 때 씀
    print("99까지의 정수중 7의배수는 {}개입니다".format(cnt))
