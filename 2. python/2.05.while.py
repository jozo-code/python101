# while 이용하기

endNum=10
n=0

while n <= endNum:
    print(n)
    n += 1

#---------------------------------------------
# pass는 나중에 코딩하겠다. 비워두겠다.

m=0
while m<10:
    pass # 나중에 코딩할게요

#----------------------------------------------
# 구구단 프로그램 만들기

gugunum = int(input("몇단? :"))
k=1
while k<10:
    result = gugunum*k
    print("{} * {} = {}".format(gugunum,k,result))
    k+=1

#----------------------------------------------

# 7의 배수의 합이 50 이상인 최초의 정수 찾기

n=0
sum=0
maxInt=0

while n<=100 and sum<=50:
    n+=1
    if n%7 ==0:
        sum+=n
        maxInt=n
    print("n:{}".format(n))

print("7의 배수의 합이 50이상인 최초의 정수:{}".format(maxInt))