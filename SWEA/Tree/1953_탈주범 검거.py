from collections import deque

delta = {1: [(1, 0), (0, 1), (-1, 0), (0, -1)],
         2: [(1, 0), (-1, 0)],
         3: [(0, -1), (0, 1)],
         4: [(-1, 0), (0, 1)],
         5: [(1, 0), (0, 1)],
         6: [(1, 0), (0, -1)],
         7: [(-1, 0), (0, -1)]}

T = int(input())
for tc in range(1, T + 1):
    N, M, r, c, h = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    Q = deque([(r, c)])
    time, ans = 0, 1
    while Q:
        i, j = Q.popleft()
        for d in delta[tunnel[i][j]]:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < N and 0 <= nj < M and tunnel:
                if tunnel[ni][nj] and visited[ni][nj] == 0:
                    if (-d[0], -d[1]) in delta[tunnel[ni][nj]]:
                        Q.append((ni, nj))
                        visited[ni][nj] = visited[i][j] + 1
                        if visited[ni][nj] <= h:
                            ans += 1
                        if time < visited[ni][nj]:
                            time = visited[ni][nj]
        if time > h:
            break
    print(f'#{tc} {ans}')