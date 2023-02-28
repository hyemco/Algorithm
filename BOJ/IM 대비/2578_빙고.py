N = 5
board = [list(map(int, input().split())) for _ in range(N)]
tm_board = list(map(list, zip(*board)))
ans = 0
for c in range(N):
    target = list(map(int, input().split()))
    for t in target:
        ans += 1
        for i in range(N):
            for j in range(N):
                if t == board[i][j]:
                    board[i][j] = 0
                    tm_board[j][i] = 0
        if c > 1:
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
                if board[k][N - 1 - k] == 0:
                    r_to_l += 1
            if l_to_r == 5:
                cnt += 1
            if r_to_l == 5:
                cnt += 1
            if cnt > 2:
                print(ans)
                break
    else:
        continue
    break