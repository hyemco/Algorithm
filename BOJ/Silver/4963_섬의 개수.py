import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    map_lst[x][y] = 0
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < h and 0 <= ny < w and map_lst[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break
    map_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    stack = []
    for i in range(h):
        for j in range(w):
            if map_lst[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)