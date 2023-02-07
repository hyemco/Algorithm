t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_cnt = 0
    for i in range(n):
        for j in range(m):
            cnt = lst[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    cnt += lst[ni][nj]
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')