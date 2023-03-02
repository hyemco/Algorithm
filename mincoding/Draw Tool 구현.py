def get_square(ny, nx, target):
    global ans
    for k in range(2, N + 1):
        cnt = 0
        for y in range(ny, ny + k):
            for x in range(nx, nx + k):
                if 0 <= y < N and 0 <= x < N and square[y][x] == target:
                    cnt += 1
                else:
                    return
        if cnt == k * k:
            ans = max(ans, k * k)


N = int(input())
Q = int(input())
square = [[0] * N for _ in range(N)]
for _ in range(Q):
    c, y1, x1, y2, x2 = map(int, input().rstrip().split())
    if y1 > y2:
        y1, y2 = y2, y1
    if x1 > x2:
        x1, x2 = x2, x1
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if square[i][j] < c:
                square[i][j] = c

ans = 1
for i in range(N):
    for j in range(N):
        if square[i][j] != 0:
            t = square[i][j]
            get_square(i, j, t)
print(ans)