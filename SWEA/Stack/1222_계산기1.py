for tc in range(1, 11):
    n = int(input())
    s = input()
    stack = []
    postfix = ''
    for i in s:
        if i.isdigit():
            postfix += i
        elif not stack:
            stack.append(i)
        else:
            postfix += stack.pop()
            stack.append(i)
    else:
        postfix += stack.pop()

    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        elif not i.isdigit():
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)

    print(f'#{tc} {stack.pop()}')