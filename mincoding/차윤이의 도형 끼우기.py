def rotation_piece(target, idx_lst):
    redirected_idx = sorted([(y - idx_lst[0][0], x - idx_lst[0][1]) for y, x in idx_lst])   # (0, 0)에 맞추기
    pieces.append(redirected_idx)
    tmp = [[0] * M for _ in range(M)]
    for i in range(M):  # 조각 리스트 90도 회전
        for j in range(M):
            tmp[j][M - i - 1] = target[i][j]
    return tmp


def count(y, x, delta):
    for dy, dx in delta:
        ny, nx = y + dy, x + dx
        if 0 <= nx < N and 0 <= ny < N:
            if puzzle[ny][nx] == '#':
                return
        else:
            return
    return True


N, M = 10, 4
piece = [list(input()) for _ in range(M)]
pieces = []
for _ in range(M):  # 4번 회전함으로썩 90도, 180도, 270도 회전 후 다시 0도까지 회전
    piece_idx = []
    for i in range(M):
        for j in range(M):
            if piece[i][j] == '$':
                piece_idx.append((i, j))
    piece = rotation_piece(piece, piece_idx)

pieces = list(set([tuple(set(piece)) for piece in pieces])) # 회전해도 같은 모양 없애주기

puzzle = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if puzzle[i][j] == '_':
            for sub_piece in pieces:
                stack = [(i, j)]
                if count(i, j, sub_piece):
                    ans += 1
print(ans)