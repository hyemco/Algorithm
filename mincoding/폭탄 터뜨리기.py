N, M = map(int, input().split())
K = int(input())
target = [list(input()) for _ in range(N)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# stack = []
for i in range(N):
    for j in range(M):
        if target[i][j] == '@':
            target[i][j] = '%'
            tmp = i, j
            for d in delta:
                for k in range(K):
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < N and 0 <= nj < M and target[ni][nj] not in '@#':
                        target[ni][nj] = '%'
                        i, j = ni, nj
                i, j = tmp
for t in target:
    print(*t, sep='')