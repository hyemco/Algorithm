t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    delta = [(1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    ans = 0

    for i in range(n):
        for j in range(m):
            cnt = 0
            if (i, j) not in [(0, 0), (0, m - 1), (n - 1, 0), (n - 1, m - 1)]:
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and lst[ni][nj] < lst[i][j]:
                        cnt += 1
                if cnt > 3:
                    ans += 1
    print(f'#{tc} {ans}')