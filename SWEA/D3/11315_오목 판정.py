delta = [(0, 1), (1, 0), (1, 1), (1, -1)]


def check():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                if i < N - 4:
                    for d in delta:
                        ni, nj = i, j
                        cnt = 0
                        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
                            cnt += 1
                            ni, nj = ni + d[0], nj + d[1]
                            if cnt >= 5:
                                return 'YES'
                else:
                    for d in delta[:2]:
                        ni, nj = i, j
                        cnt = 0
                        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
                            cnt += 1
                            ni, nj = ni + d[0], nj + d[1]
                            if cnt >= 5:
                                return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    rlt = check()

    print(f'#{tc} {rlt}')