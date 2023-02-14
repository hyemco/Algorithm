for tc in range(1, 11):
    n, s = input().split()
    lst = []
    for i in s:
        if lst:
            if lst[-1] == i:
                del lst[-1]
            else:
                lst.append(i)
        else:
            lst.append(i)
    print(f'#{tc} ', *lst, sep='')