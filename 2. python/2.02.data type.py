# 효율적인 메모리 사용을 위해 데이터를 정수형, 실수형, 문자형, 논리형 등의 자료형으로 구분해서 사용

# 정수 : int / 실수 : float / 문자열 : str / 논리형 : bool

# 논리형 자료를 문자형으로 변환


var = True
var = str(var)

# 논리형 자료를 정수나 실수로 변환하면 True는 1 False는 0으로 변환됨
var = True
var = int(var) #이렇게 하면 1이됨
var = float(var) #이렇게 하면 0이됨

# 빈문자는 데이터 없는 것이고 "", 공백문자는 공백 데이터가 있음 " " / 그래서 논리형으로 변환하면 각각 False와 True가 나옴

# 이 경우가 False
var = ""
print(var)
print*(type(var))

var = bool(var)
print(var)
print(type(var))

# 이 경우가 True
var = " "
print(var)
print*(type(var))

var = bool(var)
print(var)
print(type(var))