t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

    for i in range(n // 2 - 1, n // 2 + 1):
        for j in range(n // 2 - 1, n // 2 + 1):
            if i == j:
                board[i][j] = 2
            else:
                board[i][j] = 1

    for i in range(m):
        x, y, c = map(int, input().split())
        x -= 1
        y -= 1

        if not board[y][x]:
            board[y][x] = c
            for d in delta:
                ny, nx = y + d[0], x + d[1]
                reverse = []
                while 0 <= nx < n and 0 <= ny < n:
                    if board[ny][nx] == 0:
                        break
                    elif board[ny][nx] == c:
                        for i, j in reverse:
                            board[i][j] = c
                        break
                    else:
                        reverse.append((ny, nx))
                        ny += d[0]
                        nx += d[1]

    W, B = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                B += 1
            elif board[i][j] == 2:
                W += 1
    print(f'#{tc} {B} {W}')