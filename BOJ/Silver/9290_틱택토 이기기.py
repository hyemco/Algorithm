import sys
input = sys.stdin.readline


def game(x, y, delta):
    for dx, dy in delta:
        check = [piece, '-']
        tmp = []

        for k in range(1, 3):
            nx, ny = x + dx * k, y + dy * k
            if 0 <= nx < 3 and 0 <= ny < 3 and boards[nx][ny] in check:
                check.remove(boards[nx][ny])
                if boards[nx][ny] == '-':
                    tmp.append(nx)
                    tmp.append(ny)
            else:
                break
        if len(check) == 0:
            boards[tmp[0]][tmp[1]] = piece
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    boards = [list(input().rstrip()) for _ in range(3)]
    piece = input().rstrip()

    delta1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    delta2 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    for i in range(3):
        for j in range(3):
            if boards[i][j] == piece:
                if i == j or i + j == 2:
                    if game(i, j, delta2):
                        break
                else:
                    if game(i, j, delta1):
                        break
        else:
            continue
        break

    print(f'Case {tc}: ')
    for board in boards:
        print(*board, sep='')