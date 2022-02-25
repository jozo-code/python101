from collections import Counter


def solution(s):
    li = []
    for i in enumerate(s):
        a=list(i)[1]
        li.append(a)
    li2 = sorted((-count,str) for str, count in Counter(li).items())
    result=[]
    for count, str in li2:
        for i in range(-count):
            result.append(str)
    answer = "".join(result)
    return answer

print(solution("aaAAcccbbbBB"))