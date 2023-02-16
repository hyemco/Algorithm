for tc in range(1, 11):
    tc_l = int(input())
    s = input()
    stack = []
    postfix = ''

    for i in s:
        if i.isdigit():
            postfix += i
        else:
            if i == '(':
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':
                    postfix += stack.pop()
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
    while stack:
        postfix += stack.pop()
    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        else:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
    print(f'#{tc} {stack.pop()}')