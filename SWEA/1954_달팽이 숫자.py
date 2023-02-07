t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    lst = [[0] * n for _ in range(n)]
    i, j = 0, 0
    k = 0
    for num in range(1, (n * n) + 1):
        lst[i][j] = num
        i += di[k]
        j += dj[k]

        if i < 0 or j < 0 or i >= n or j >= n or lst[i][j] != 0:
            i -= di[k]
            j -= dj[k]
            k = (k + 1) % 4
            i += di[k]
            j += dj[k]
    print(f'#{tc}')
    for i in lst:
        print(*i)