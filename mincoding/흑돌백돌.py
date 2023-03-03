N = int(input())
board = [['_'] * 8 for _ in range(8)]
for k in range(N):
    x, y = map(int, input().split())
    if k % 2:
        board[7 - y][x] = 'O'
    else:
        board[7 - y][x] = '@'

    delta = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    i, j = 7 - y, x
    for di, dj in delta:
        ni, nj = i + di, j + dj
        stack = []
        if 0 <= ni < 8 and 0 <= nj < 8:
            if board[i][j] == '@' and board[ni][nj] == 'O':
                while 0 <= ni < 8 and 0 <= nj < 8:
                    if board[ni][nj] == '_':
                        break
                    elif board[ni][nj] == '@':
                        for y, x in stack:
                            board[y][x] = '@'
                        break
                    stack.append((ni, nj))
                    ni, nj = ni + di, nj + dj
            elif board[i][j] == 'O' and board[ni][nj] == '@':
                while 0 <= ni < 8 and 0 <= nj < 8:
                    if board[ni][nj] == '_':
                        break
                    elif board[ni][nj] == 'O':
                        for y, x in stack:
                            board[y][x] = 'O'
                        break
                    stack.append((ni, nj))
                    ni, nj = ni + di, nj + dj
for b in board:
    print(*b, sep='')