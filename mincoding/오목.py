def check():
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                for d in delta:
                    cnt = []
                    ni, nj = i, j
                    while 0 <= ni < N and 0 <= nj < N:
                        if board[i][j] == board[ni][nj]:
                            cnt.append((ni + 1, nj + 1))
                            if len(cnt) > 5:
                                break
                        else:
                            break
                        ni += d[0]
                        nj += d[1]
                    if len(cnt) == 5:
                        if 0 <= i - d[0] < N and 0 <= j - d[1] < N and board[i][j] == board[i - d[0]][j - d[1]]:
                            break
                        else:
                            cnt.sort(key=lambda x: x[1])
                            print(board[i][j])
                            print(*cnt[0])
                            return True
    return False


N = 19
board = [list(map(int, input().split())) for _ in range(N)]

delta = [(0, 1), (1, 0), (1, 1), (1, -1)]

if not check():
    print(0)