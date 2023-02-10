m, n = map(int, input().split())
board = [list(input()) for _ in range(m)]
ans = []
for i in range(m - 7):
    for j in range(n - 7):
        draw_b = 0
        draw_w = 0
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if (r + c) % 2:
                    if board[r][c] != 'W':
                        draw_w += 1
                    elif board[r][c] != 'B':
                        draw_b += 1
                else:
                    if board[r][c] != 'B':
                        draw_w += 1
                    elif board[r][c] != 'W':
                        draw_b += 1
        ans.append(draw_b)
        ans.append(draw_w)
print(min(ans))