def solution(nums, k):
    nums_str = "".join(list(map(str,nums)))
    nums_str_spl = nums_str.split("0")
    n_lst =[]
    for i in nums_str_spl:
        n = len(i)
        n_lst.append(n)

    sum_lst =[]
    for i in range(len(n_lst)-k):
        temp=0
        for j in range(1,k+1):
            temp = temp + n_lst[i+j]
        temp2 = temp+k
        kk = n_lst[i]+temp2
        sum_lst.append(kk)
    answer = max(sum_lst)
    return answer


    # 시간초과로 실패


def solution(nums, k):
    nums_str = "".join(list(map(str,nums)))
    nums_str_spl = nums_str.split("0")
    n_lst =[]
    for i in nums_str_spl:
        n = len(i)
        n_lst.append(n)

    sum_lst =[]
    for i in range(len(n_lst)-k):
        sum_lst.append(sum(n_lst[i:i+k+1])+k)
    answer = max(sum_lst)
    return answer

    # 두번째도 실패