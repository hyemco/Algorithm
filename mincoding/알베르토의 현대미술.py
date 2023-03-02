N = int(input())
canvas = [['_'] * 6 for _ in range(6)]

delta_L = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
delta_R = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

for _ in range(N):
    idx, d = input().split()
    ni, nj = 5, int(idx)
    paint = 1
    if d == 'L':
        for d in delta_L:
            while 0 <= ni < 6 and 0 <= nj < 6:
                if canvas[ni][nj] == '_':
                    canvas[ni][nj] = paint
                elif canvas[ni][nj] > paint:
                    canvas[ni][nj] = paint
                ni, nj = ni + d[0], nj + d[1]
                paint += 1
            ni, nj = ni - d[0], nj - d[1]
            paint -= 1
    if d == 'R':
        for d in delta_R:
            while 0 <= ni < 6 and 0 <= nj < 6:
                if canvas[ni][nj] == '_':
                    canvas[ni][nj] = paint
                elif canvas[ni][nj] > paint:
                    canvas[ni][nj] = paint
                ni, nj = ni + d[0], nj + d[1]
                paint += 1
            ni, nj = ni - d[0], nj - d[1]
            paint -= 1
for c in canvas:
    print(*c, sep='')