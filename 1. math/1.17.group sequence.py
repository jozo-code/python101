# 수열을 보고 n 번째 항을 출력하는 프로글매을 만들자
# an ={1,1,2,1,2,3,1,2,3,4,1,2,3,4,5,....}



inputN=int(input("n항 입력: "))
flag = True #while문에 사용하는 변수
n=1; nCnt=1; seaerhN=0

while flag : #true이면 계속 돈다
    for i in range(1,n+1):
        if i==n:
            print("{} ".format(i),end="")
        else:
            print("{}, ".format(i), end="")
        nCnt +=1

        if nCnt > inputN: # 총항의수(nCnt)가 inputN보다 커지면 멈춤
            searchN = i
            flag = False # 반복문 멈춤
            break
    print()
    n+=1
print("{}항:{} ".format(inputN,searchN))
