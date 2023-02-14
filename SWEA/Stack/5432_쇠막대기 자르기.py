t = int(input())
for tc in range(1, t + 1):
    lst = list(input())
    stick = 0
    cnt = 0
    l = len(lst)
    i = 0
    while i < l:
        if lst[i] == '(' and lst[i+1] == ')':
            cnt += stick
            i += 2
        elif lst[i] == '(':
            stick += 1
            i += 1
        else:
            cnt += 1
            stick -= 1
            i += 1
    print(f'#{tc} {cnt}')