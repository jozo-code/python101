# 문제
# 지민이는 전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.

# 입력
# 첫째 줄에 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 공백으로 구분해 출력한다.

pages = int(input()) # 전체 페이지수

sep_num=[] # 떼어진 숫자 리스트

for page in range(1,pages+1):
    for num in enumerate(str(page)):
        sep_num.append(list(num)[1])

for i in range(10):
    print(sep_num.count(str(i)),end=" ")
