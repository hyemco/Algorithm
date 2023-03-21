import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    Q = deque([(0, 0, 0)])
    visited[0][0] = 1, 1

    while Q:
        x, y, wall = Q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][wall]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][wall]:
                if map_lst[nx][ny] == 0:
                    Q.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1

                if wall == 0 and map_lst[nx][ny] == 1:
                    Q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][wall] + 1
    return -1


N, M = map(int, input().split())
map_lst = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = bfs()
print(ans)