# 현수네 반은 오늘 회장선거를 합니다. 현수네 반 N명의 학생은 각자 자기가 좋아하는 학생을 회장후보로 추천합니다.
# 한 학생이 여러명을 추천할 수 있습니다.
# 추천횟수가 k번 이상인 학생들만 회장선거에 출마할 수 있습니다.
# 회장선거에 출마한 학생들은 자기를 추천해준 학생들에게 감사의 이메일을 보내기로 했습니다.
# 0번 학생부터 N-1번 학생까지 각 학생이 감사이메일을 받는 횟수를 알아내는 프로그램을 작성하세요.
# 만약 0번 학생이 3번학생을 추천 했다면 [0, 3]의 순써쌍 입력정보가 들어옵니다.
# 만약 반 학생이 4명이고, 각 학생의 추천정보가 [0, 1], [0, 3], [1, 2], [2, 0], [2, 3], [3, 0]이고,
# k=2이면 회장후보는 0번과 3번입니다.
# 그리고 각 학생이 받는 감사이메일 횟수는 0번은 1통, 1번은 0통, 2번은 2통, 3번은 1통입니다.


# ▣ 입력설명
# 첫 번째 줄에 반 학생수 n(3<=n<=100)과 투표정보 순서쌍 개수인 m이 입력됩니다.
# 두 번째 줄부터 m줄에 걸쳐 추천정보 순서쌍이 입력됩니다.
# 각 학생은 추천을 할 수도 있고, 하지 않을 수도 있습니다.
# 마지막 줄에 회장선거에 출마할 수 있는 추천횟수 k가 입력됩니다.

# ▣ 출력설명
# 각 학생이 받는 감사메일 횟수를 0번 학생부터 차례대로 출력합니다.


# ▣ 입력예제 1
# 4 6
# 0 1
# 0 3
# 1 2
# 2 0
# 2 3
# 3 0
# 2

# ▣ 출력예제 1
# 1 0 2 1

# 반환값 설명 : 0번 학생은 1통, 1번은 0통, 2번은 2통, 3번은 1통입니다.



# 여기서 부터 시작
n,rec_n = map(int, input().split(" "))

rec_result = []
for i in range(rec_n): 
    result = list(map(int, input().split(" ")))
    rec_result.append(result)
cutoff = int(input())

#a = 후보자
a_list = []
# b = 선발자
b_list = []
for j in range(len(rec_result)):
    a_list.append(rec_result[j][1])
for k in range(n):
    if a_list.count(k) >= cutoff :
        b_list.append(k)
print(b_list)

# # 감사인사 돌리기 수정 코드
def letter(n):
    thank =[]
    for x,y in rec_result:
        for z in b_list:
            if y == z:
                thank.append(x)
    return thank.count(n)

for x in range(n):
    print(str(letter(x))+" ",end="")


# 감사인사 돌리기 틀린 코드 이유 점검할 것---------------
# for j in range(n):
#     letter = 0
#     for i in range(rec_n):
#         if rec_result[i][0]==j:
#             if rec_result[i][1] in b_list:
#                 letter =+1
#     print(letter, end=" ")
