N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    for _ in range(4):
        di, dj = delta[(d + 3) % 4]
        ni, nj = r + di, c + dj
        d = (d + 3) % 4
        if room[ni][nj] == 0:
            r, c = ni, nj
            break
    else:
        di, dj = delta[d]
        ni, nj = r - di, c - dj
        if room[ni][nj] == 1:
            break
        else:
            r, c = ni, nj
print(cnt)