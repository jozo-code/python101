# 순열 구하기

# nPr = n(n-1)(n-2)(n-r+1)

numN=int(input("num 입력:"))
numR=int(input("numR 입력:"))
result=1

#range(2,7) # 2~6까지
#range(7,2,-1) #7~3까지

for n in range(numN, (numN-numR),-1) :# 세번째 -1은 1씩 차감하는 조치임
                            #for n in range((numN-numR)+1,numN+1): #이렇게 쓴 거랑 똑같은데 왜그런지 모르겠네?
    print("numN:{}".format(numN))
    print("n:{}".format(n))
    result = result*n

print("result:{}".format(result))

