for tc in range(1, 11):
    l, n = input().split()
    lst = []
    for i in n:
        if lst:
            if lst[-1] == int(i):
                del lst[-1]
            else:
                lst.append(int(i))
        else:
            lst.append(int(i))
    print(f'#{tc}', end=' ')
    print(*lst, sep='')