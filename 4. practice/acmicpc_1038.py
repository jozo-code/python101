# 현재의 수가 0~8일 경우: 1을 더한다.
# 아래 자릿수부터 검사했을 때 바로 위 자릿수와 2 이상 차이나는 수가 있을 경우: 해당 자릿수에 1을 더하고 아래 자릿수들을 최소화한다.
# 위의 경우에 해당하지 않는데 맨 위의 자릿수가 9가 아닐 경우: 맨 윗 자릿수에 1을 더하고 아래 자릿수들을 최소화한다.
# 위의 경우에 해당하지 않아 맨 위 자릿수가 9일 경우: 현재 수와 같은 길이의 최소 감소하는 수를 만들고 최소의 맨 윗자리 수를 붙인다.

def solution(n):
    num = 0
    for _ in range(n):
        if num < 9:
            num += 1
            continue
        str_num = list(str(num))
        flag = False
        for i in range(len(str_num) - 1, -1, -1):
            if int(str_num[i - 1]) - int(str_num[i]) > 1:
                str_num[i] = str(int(str_num[i]) + 1)
                str_num = str_num[:i + 1] + list(map(str, range(len(str_num) - i - 2, -1, -1)))
                num = int(''.join(str_num))
                flag = True
                break
        if not flag:
            if str_num[0] != '9':
                str_num = list(str(int(str_num[0]) + 1)) + list(map(str, range(len(str_num) - 2, -1, -1)))
            else:
                str_num = list(map(str, range(len(str_num) - 1, -1, -1)))
                str_num.insert(0, str(int(str_num[0]) + 1))
            num = int(''.join(str_num))
    return num

# 32



n = int(input())
print(-1 if n > 1022 else solution(n))