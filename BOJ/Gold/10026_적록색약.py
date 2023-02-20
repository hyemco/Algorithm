import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if lst[x][y] == lst[nx][ny] and visited[nx][ny] == 0:
                dfs(nx, ny)


n = int(sys.stdin.readline())
lst = [list(map(str, sys.stdin.readline())) for _ in range(n)]
non_cw = cw = 0

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            non_cw += 1
            dfs(i, j)

for i in range(n):
    for j in range(n):
        if lst[i][j] == 'R':
            lst[i][j] = 'G'

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cw += 1
            dfs(i, j)
print(non_cw,cw)