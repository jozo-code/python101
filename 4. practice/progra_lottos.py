# lotto 번호는 6개, 당첨 숫자도 6개, |7-(맞은 숫자)|가 순위임
# 낙서는 0으로 표시하기 때문에 0의 개수를 생각해보면
# |7-(맞은숫자)|이게 최저 순위이고 |7-(맞은숫자)-(0의개수)|가 최고 순위임


lottos = list(map(int, input().split(","))) # 리스트로 숫자 입력
win_nums =list(map(int, input().split(",")))


# 리스트에서 같은 값 찾기
win_get = list(set(lottos)&set(win_nums))
cnt_win_get = len(win_get)
cnt_0 = lottos.count(0)

if cnt_win_get ==0 and cnt_0 ==0:
    win_max = 6
else:
    win_max = abs(7-cnt_win_get-cnt_0)

if cnt_0 == 6:
    win_min = 6
else:
    win_min = abs(7-cnt_win_get)

print(win_max, win_min)