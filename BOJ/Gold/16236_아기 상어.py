import sys
input = sys.stdin.readline


def dfs(x, y):
    visited = [[False] * N for _ in range(N)]

    Q = [(x, y)]
    cnt_time = 0

    while Q:
        times = []
        tmp = []
        for x, y in Q:
            if visited[x][y]:
                continue

            visited[x][y] = True

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if 0 < fishes[nx][ny] < size:
                        times.append((nx, ny))
                    elif fishes[nx][ny] <= size:
                        tmp.append((nx, ny))
        if times:
            times.sort()
            p, q = times[0]
            fishes[p][q] = 0
            return cnt_time + 1, p, q
        cnt_time += 1
        Q = tmp
    return 0, 0, 0


N = int(input())
fishes = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if fishes[i][j] == 9:
            x, y = i, j
            fishes[x][y] = 0

ans = cnt = 0
size = 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    time, x, y = dfs(x, y)
    if time == 0:
        break
    else:
        cnt += 1
        if size == cnt:
            size += 1
            cnt = 0
        ans += time
print(ans)