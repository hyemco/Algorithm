def solution(board):
    answer = 0
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(len(board)):
        for j in range(len(board)):
            tmp = 0
            if board[i][j] == 1:
                continue
            for d in delta:
                n_i, n_j = i + d[0], j + d[1]
                if -1 < n_i < len(board) and -1 < n_j < len(board):
                    if board[n_i][n_j] == 1:
                        tmp = 1
                        break
            if tmp == 0:
                answer += 1    
    return answer