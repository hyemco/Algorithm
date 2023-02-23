from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [[-1] * M for _ in range(N)]
    Q = deque()
    for i in range(N):
        map_info = input()
        for j in range(M):
            if map_info[j] == 'W':
                Q.append((i, j))
                visited[i][j] = 0

    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while Q:
        i, j = Q.popleft()
        for d in delta:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == -1:
                    Q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

    ans = 0
    for k in visited:
        ans += sum(k)
    print(f'#{tc} {ans}')