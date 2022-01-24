# 진법 변환에 bin(), oct(), hex() 이용 가능, 변환 결과는 문자열 형식임

# 숫자 30을 각각 2진수, 8진수, 16진수로 변환하는 방식은 아래와 같음

dNum = 30

print('2진수:{}'.format(bin(dNum)))
print('8진수:{}'.format(oct(dNum)))
print('16진수:{}'.format(hex(dNum)))


# 이렇게도 할 수 있음

print('2진수:{}'.format(format(dNum, '#b')))


# 이렇게도 할 수 있음

print('{0:#b}, {0:#o}, {0:#x}'.format(dNum))


# <#> 빼고 싶으면 이렇게도 할 수 있음

print('2진수:{}'.format(format(dNum, 'b')))


# x진수를 10진수로 변환하는 방법

print('2진수(0b1110)->10진수({})'.format(int('0b1110',2)))
