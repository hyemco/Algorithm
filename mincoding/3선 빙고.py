n = 5

board = [list(map(int, input().split())) for _ in range(n)]
tm_board = list(map(list, zip(*board)))
target = sum(list(list(map(int, input().split())) for _ in range(n)), [])

for t in range(len(target)):
    for i in range(n):
        for j in range(n):
            if board[i][j] == target[t]:
                board[i][j] = 0
                tm_board[j][i] = 0

    if t > 12:
        cnt = 0
        for row in board:
            if sum(row) == 0:
                cnt += 1
        for row in tm_board:
            if sum(row) == 0:
                cnt += 1
        l_to_r = 0
        r_to_l = 0
        for k in range(5):
            if board[k][k] == 0:
                l_to_r += 1
            if board[k][n - 1 - k] == 0:
                r_to_l += 1
        if l_to_r == 5:
            cnt += 1
        if r_to_l == 5:
            cnt += 1

        if cnt >= 3:
            print(target[t])
            break