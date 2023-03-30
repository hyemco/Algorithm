def dfs(cnt, x, y, num):
    global ans

    if cnt == 7:
        numbers.add(num)
        return

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            dfs(cnt + 1, nx, ny, (num * 10) + board[nx][ny])


T = int(input())
for tc in range(1, T + 1):
    N = 4
    board = [list(map(int, input().split())) for _ in range(N)]

    numbers = set()
    for i in range(N):
        for j in range(N):
            dfs(1, i, j, board[i][j])

    ans = len(numbers)
    print(f'#{tc} {ans}')