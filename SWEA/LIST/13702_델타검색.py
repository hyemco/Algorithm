for tc in range(1, 11):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    ans += abs(lst[i][j] - lst[ni][nj])

    print(f'#{tc} {ans}')