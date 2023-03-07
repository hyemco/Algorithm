import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())


tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
Q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                Q.append((i, j, k))

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

while Q:
    z, x, y = Q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomato[nz][nx][ny] == 0:
            tomato[nz][nx][ny] = tomato[z][x][y] + 1
            Q.append((nz, nx, ny))

ans = 0
for t in tomato:
    for i in t:
        if i.count(0) > 0:
            print(-1)
            exit(0)
        ans = max(ans, max(i))
print(ans - 1)