N, M = 100, 10
paper = [[0] * N for _ in range(N)]
Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    for i in range(q, q + M):
        for j in range(p, p + M):
            paper[i][j] = 1

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0
for i in range(N):
    for j in range(N):
        if paper[i][j] == 1:
            cnt = 0
            ans += 4
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    ans -= paper[ni][nj]
print(ans)