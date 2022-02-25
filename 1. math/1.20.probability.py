# 조합 : 순서 없이 뽑는 경우의 수
# nCr = nPr/r! = n!/r!(n-r)!

# 확률 구하기 문제 박스에 꽝이 적힌 종이가 4장 선물이 3장 있을 때 꽝 2장과 선물 1장을 뽑는 확률 출력

# 함수선언
def proFun():

    numN = int(input("numN 입력: "))
    numR = int(input("numR 입력: "))

    resultP =1
    resultR =1
    resultC =1

    # 순열 구하기
    for n in range(numN, (numN-numR), -1):
        resultP = resultP*n
    print("resultP: {}".format(resultP))


    # 조합구하기
    for n in range(numR, 0, -1):
        resultR= resultR*n
    print("resultR: {}".format(resultR))
    resultC = int(resultP/resultR)
    print("resultC: {}".format(resultC))

    #함수를 사용했으면 반환해야함

    return resultC

sample = proFun()
print("sample: {}".format(sample))

event1 = proFun()
print("sample: {}".format(event1))

event2 = proFun()
print("sample: {}".format(event2))

prob = event1*event2/sample
print("prob: {}%".format(round(prob*100,2))) # round 소수점 어디까지 나타낼지 지정, 지금은 둘째자리까지


