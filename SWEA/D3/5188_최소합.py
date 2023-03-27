def brute_force(x, y, total):
    global ans
    total += lst[x][y]
    if ans < total:
        return
    if x == y == N - 1:
        if ans > total:
            ans = total
        return

    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            brute_force(nx, ny, total)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    delta = [(1, 0), (0, 1)]

    ans = 13 * 13 * 10
    brute_force(0, 0, 0)
    print(f'#{tc} {ans}')
