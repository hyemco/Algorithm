N = int(input())
target = int(input())

snail = [[0] * N for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
k = 0

num = N * N
i, j = 0, 0
tx, ty, = 0, 0

while num > 0:
    snail[i][j] = num
    if num == target:
        ty, tx = i + 1, j + 1

    # snail 범위를 벗어나거나 이미 숫자가 채워진 경우 방향 전환
    if i + dy[k] < 0 or i + dy[k] >= N or j + dx[k] < 0 or j + dx[k] >= N or snail[i + dy[k]][j + dx[k]] != 0:
        k = (k + 1) % 4

    i += dy[k]
    j += dx[k]
    num -= 1

for s in snail:
    print(*s)

print(ty, tx)