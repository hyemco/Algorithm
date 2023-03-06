T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j]:
                cnt = lst[i][j]
                for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
                    for k in range(1, lst[i][j] + 1):
                        ni, nj = i + di * k, j + dj * k
                        if 0 <= ni < N and 0 <= nj < M:
                            cnt += lst[ni][nj]
                ans = max(ans, cnt)
    print(f'#{tc} {ans}')