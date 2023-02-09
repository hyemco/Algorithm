t = int(input())
for tc in range(1, t + 1):
    s = input()
    l = len(s) * 4 + 1
    lst = [['.'] * l for _ in range(5)]

    for i in range(5):
        if i == 0 or i == 4:
            for j in range(2, l, 4):
                lst[i][j] = '#'
        if i == 1 or i == 3:
            for j in range(1, l, 2):
                lst[i][j] = '#'
        if i == 2:
            for j in range(0, l, 4):
                lst[i][j] = '#'
            idx = 0
            for j in range(2, l, 4):
                lst[i][j] = s[idx]
                idx += 1
    for i in lst:
        print(*i, sep='')