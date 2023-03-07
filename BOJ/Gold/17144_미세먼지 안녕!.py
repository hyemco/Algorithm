def find_dust():
    delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    dust_lit = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if rooms[i][j] != 0 and rooms[i][j] != -1:
                dust = 0
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and rooms[ni][nj] != -1:
                        dust_lit[ni][nj] += rooms[i][j] // 5
                        dust += rooms[i][j] // 5
                rooms[i][j] -= dust

    for i in range(R):
        for j in range(C):
            rooms[i][j] += dust_lit[i][j]


def air_move_up():
    delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    d = tmp = 0
    i, j = up, 1
    while True:
        ni, nj = i + delta[d][0], j + delta[d][1]
        if i == up and j == 0:
            break
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            d += 1
            continue
        rooms[i][j], tmp = tmp, rooms[i][j]
        i, j = ni, nj


def air_move_down():
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = tmp = 0
    i, j = down, 1
    while True:
        ni, nj = i + delta[d][0], j + delta[d][1]
        if i == down and j == 0:
            break
        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            d += 1
            continue
        rooms[i][j], tmp = tmp, rooms[i][j]
        i, j = ni, nj


R, C, T = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if rooms[i][0] == -1:
        up = i
        down = i + 1
        break

for _ in range(T):
    find_dust()
    air_move_up()
    air_move_down()

ans = 0
for i in range(R):
    for j in range(C):
        if rooms[i][j] > 0:
            ans += rooms[i][j]
print(ans)