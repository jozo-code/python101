# 길이가 $n$인 문자열 $S=s_1s_2\cdots s_n$와 길이가 $n$인 양의 정수 수열 $A=(a_1, a_2, \cdots a_n)$를 이용하여 다음과 같이 새로운 문자열 $T$를 만들 수 있다.

#  $X_0$는 빈 문자열이다.
#  $X_i = X_{i-1} s_i X_{i-1} s_i \cdots s_i X_{i-1}$, $s_i$는 $a_i$번, $X_{i-1}$은 $a_i + 1$번 등장한다.
#  $T = X_n$이다.
# 예를 들어 $S=abc$고, $A=(1,2,1)$이면 $X_1=a, X_2=ababa, X_3=T=ababacababa$가 된다.

# 문자의 개수를 기준으로 찾으면 될 것 같음
# 0~n 번째 문자열이 S에 들어있음
# 0~n 번째 문자열의 반복 횟수가 A에 들어있음
# A개 만큼 현재 문자열을 넣고 양옆에 A+1개의 이전 문자열이 들어감
# 처음에 위치하는 현재 문자열들만 찾으면 이전 문자열도 알 수 있고, 반복 횟수도 알수 있음
    #절반을 나눈 것과 비교
    # 3으로 나눈 것과 비교
    # 4로 나눈 것과 비교 쭉쭉 나가서 n개로 나눈 것과 비교 하면 될듯

T = str(input()) # 전체문자열 T

for i in range(2,len(T)):
    x_num = (len(T)-(i-1))
    if x_num % i == 0:
        index = x_num//i
        if T[:index] == T[-index:]:
            x_str = T[:index]
            p_str = T[index]
            a_p = i-1
            print(x_str, p_str, a_p)
            break