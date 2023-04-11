from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    Q = deque()
    distance = [[-1] * (w + 2) for _ in range(h + 2)]
    Q.append([x, y])
    distance[x][y] = 0
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if distance[nx][ny] == -1:
                    if jail[nx][ny] == '.':
                        distance[nx][ny] = distance[x][y]
                        Q.appendleft([nx, ny])
                    elif jail[nx][ny] == '#':
                        distance[nx][ny] = distance[x][y] + 1
                        Q.append([nx, ny])

    return distance


def new_map():
    for i in jail:
        i.insert(0, '.')
        i.append('.')
    jail.insert(0, ['.' for _ in range(w+2)])
    jail.append(['.' for _ in range(w+2)])


T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    jail = [list(input().strip()) for _ in range(h)]

    new_map()

    tmp = []
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if jail[i][j] == '$':
                tmp.extend([i, j])
                jail[i][j] = '.'

    x1, y1, x2, y2 = tmp
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    point1 = bfs(0, 0)
    point2 = bfs(x1, y1)
    point3 = bfs(x2, y2)

    ans = sys.maxsize
    for i in range(h + 2):
        for j in range(w + 2):
            if point1[i][j] != -1 and point2[i][j] != -1 and point3[i][j] != -1:
                cnt = point1[i][j] + point2[i][j] + point3[i][j]
                if jail[i][j] == '#':
                    cnt -= 2
                ans = min(ans, cnt)
    print(ans)