#72에 x를 곱하면 y의 제곱이 된다고 할 때, X에 해당하는 가장 작은 정수를 구하자


inputNumber = int(input("1보다 큰 정수 입력: "))

n=2
searchNumbers =[] #리스트 만들기
while n <= inputNumber:
    if inputNumber % n == 0: #소인수분해하는 과정
        print("소인수:{}".format(n))
        if searchNumbers.count(n) == 0: #searchNumbers에 n의 개수를 세서 0개 이면
            searchNumbers.append(n) #searchNumbers 리스트에 n을 추가한다.

            #여기서부터

        elif searchNumbers.count(n) ==1: #n이 하나 들어있다면 
            searchNumbers.remove(n) #n을 지워버린다.

            #여기까지는 지워도 똑같이 작동

        inputNumber /= n #나눠서 계속 소인수분해하기
    else:
        n = n+1 #또는 n+=1 이라고 써도 됨

print("searchNumbers: {}".format(searchNumbers)) #searchNumbers에 담긴 숫자를 출력한다.

