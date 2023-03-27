import sys
input = sys.stdin.readline


def dfs(nx, ny, hp, cnt):
    global ans
    for x, y in milks:
        if town[x][y] == 2:
            distance = abs(nx - x) + abs(ny - y)
            if distance <= hp:
                town[x][y] = 0
                dfs(x, y, hp + (H - distance), cnt + 1)
                town[x][y] = 2
    if abs(nx - hx) + abs(ny - hy) <= hp:
        ans = max(ans, cnt)


N, M, H = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]

milks = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            hx, hy = i, j
        elif town[i][j] == 2:
            milks.append((i, j))

ans = 0
dfs(hx, hy, M, 0)
print(ans)
