string = input()
stack = []
for i in string:
    print(i)
    if i == ')':
        while stack.pop() != '(':
            print("while문 입니다 stack 값:{}".format(stack))
            pass
    else:
        stack.append(i)
        print("else문 입니다 stack 값:{}".format(stack))




