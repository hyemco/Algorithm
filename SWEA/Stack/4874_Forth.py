t = int(input())
for tc in range(1, t + 1):
    inp = list(input().split())
    stack = []
    for i in inp:
        if i.isdigit():
            stack.append(int(i))
        elif i == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack.pop()}')
            else:
                print(f'#{tc} error')
        else:
            if len(stack) < 2:
                print(f'#{tc} error')
                break
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(b * a)
                elif i == '/':
                    stack.append(b // a)