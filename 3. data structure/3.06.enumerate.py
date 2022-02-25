# enumerate 함수로 아이템 열거하기

sports = ['농구','야구','축구','피구','테니스']


for i in range( len(sports)):
    print("{}:{}".format(i,sports[i]))

# 위의 코드를 enumerate를 사용하면

for idx, value in enumerate(sports):
    print("{}:{}".format(idx,value))


# 문자열에도 사용가능
str = "what you say"
for value in enumerate(str):
    print("{}".format(value))


# enumerate 함수로 아이템 열거하기


sports = ['농구','야구','축구','피구','테니스']
favoritSport = input("좋아하는 스포츠가 무엇인가요?")
bestSportIdx=0
for idx, value in enumerate(sports):
    if value == favoritSport:
        bestSportIdx = idx+1
print("{}는 {}번째에 있습니다.".format(favoritSport,bestSportIdx))

