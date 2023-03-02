def sand_count(di, dj, direction, time):
    global ans, si, sj

    for _ in range(time):
        si += di
        sj += dj
        if sj < 0:
            break

        total = 0
        for di, dj, r in direction:
            ni = si + di
            nj = sj + dj
            if r == 0:
                new_sand = sand[si][sj] - total
            else:
                new_sand = int(sand[si][sj] * r)
                total += new_sand

            if 0 <= ni < N and 0 <= nj < N:
                sand[ni][nj] += new_sand
            else:
                ans += new_sand


to_left = [(-1, -1, 0.1), (1, -1, 0.1), (-1, 0, 0.07), (-2, 0, 0.02),(1, 0, 0.07),
           (2, 0, 0.02), (-1, 1, 0.01), (1, 1, 0.01), (0, -2, 0.05),  (0, -1, 0)]
to_down = [(-y, x, r) for x, y, r in to_left]
to_right = [(x, -y, r) for x, y, r in to_left]
to_up = [(y, x, r) for x, y, r in to_left]

N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

si = sj = N // 2
ans = 0
for i in range(1, N + 1):
    if i % 2:
        sand_count(0, -1, to_left, i)
        sand_count(1, 0, to_down, i)
    else:
        sand_count(0, 1, to_right, i)
        sand_count(-1, 0, to_up, i)
print(ans)
