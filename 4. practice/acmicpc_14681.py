# 백분 14681 사분면 고르기 문제


x = int(input())
y = int(input())


# x가 0보다 클 때 y가 0보다 크면 1 작으면 4
# x가 0보다 작을 때 y가 0보다 크면 2 작으면 3


if x > 0 and y >0:
    print(1)
elif x > 0 and y <0 :
    print(4)
elif x < 0 and y <0 :
    print(3)
else :
    print(2)
