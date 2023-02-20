from collections import deque

res = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for m in range(10):
    tmp = 0
    _ = input()
    li = []
    visit = [[0] * 16 for i in range(16)]
    for i in range(16):
        li.append(list(input()))
    q = deque()
    q.append((1, 1))
    visit[1][1] = 1
    while q:
        x, y = q.popleft()
        for s in range(4):
            nx = x+dx[s]
            ny = y+dy[s]
            if 0 <= nx <= 15 and 0 <= ny <= 15:
                if li[nx][ny] == "3":
                    tmp = 1
                    break
                if li[nx][ny] == "0" and visit[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
    res.append(tmp)
for i in range(len(res)):
    print(f'#{i + 1} {res[i]}')