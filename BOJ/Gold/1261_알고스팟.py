import sys, heapq
input = sys.stdin.readline


def dijkstra():
    Q = []
    heapq.heappush(Q, (0, 0, 0))
    visited[0][0] = True

    while Q:
        cnt, x, y = heapq.heappop(Q)
        if x == N - 1 and y == M - 1:
            return cnt

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True

                if maze[nx][ny]:
                    heapq.heappush(Q, (cnt + 1, nx, ny))
                else:
                    heapq.heappush(Q, (cnt, nx, ny))


M, N = map(int, input().rstrip().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = dijkstra()
print(ans)