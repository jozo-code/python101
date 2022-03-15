import sys

N = int(sys.stdin.readline())

queue = []

for _ in range(N) :
    order = sys.stdin.readline().split() #입력 받는데 split해서 입력 받기
    text = order[0] #명령어 받기
        
    #text가 push라면
    if text =="push" :
        value = order[1]
        queue.append(value)
    
    #text가 pop이라면
    elif text=="pop" :
        if len(queue)==0 :
            print(-1)
        else :
            print(queue.pop(0))
    
    #text가 size라면
    elif text=="size" :
        print(len(queue))
    
    #text가 empty라면
    elif text=="empty" :
        if len(queue)==0 :
            print(1)
        else : 
            print(0)
    
    #text가 front라면
    elif text=="front" : 
        if len(queue)==0 : 
            print(-1)
        else : 
            print(queue[0])

    #text가 back라면
    elif text=="back" : 
        if len(queue)==0 : 
            print(-1)
        else : 
            print(queue[-1])