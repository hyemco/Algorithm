from collections import deque


def bfs(x, y):
    visited[x][y] = 0
    Q = deque()
    Q.append((x, y))
    while Q:
        i, j = Q.popleft()
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = 0
                if graph[i][j] < graph[ni][nj]:
                    diff = graph[ni][nj] - graph[i][j]
                if visited[i][j] + 1 + diff < visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1 + diff
                    Q.append((ni, nj))
    return visited[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[10000000] * N for _ in range(N)]

    ans = bfs(0, 0)
    print(f'#{tc} {ans}')