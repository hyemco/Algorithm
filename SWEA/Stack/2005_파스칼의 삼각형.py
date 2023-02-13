t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i - 1][j - 1] + lst[i - 1][j]
    print(f'#{tc}')
    for i in lst:
        ans = [x for x in i if x != 0]
        print(*ans)