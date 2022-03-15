import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N) :
    order = sys.stdin.readline().split() 
    text = order[0] 
        
    #text가 push라면
    if text =="push" :
        value = order[1]
        stack.append(value)
    
    #text가 pop이라면
    elif text=="pop" :
        if len(stack)==0 :
            print(-1)
        else :
            print(stack.pop())
    
    #text가 size라면
    elif text=="size" :
        print(len(stack))
    
    #text가 empty라면
    elif text=="empty" :
        if len(stack)==0 :
            print(1)
        else : 
            print(0)
    
    #text가 top이라면
    elif text=="top" : 
        if len(stack)==0 : 
            print(-1)
        else : 
            print(stack[-1])