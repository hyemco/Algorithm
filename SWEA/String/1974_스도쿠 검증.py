def sudoku(square):
    for i in range(9):
        num_r = [0] * 9
        num_c = [0] * 9
        for j in range(9):
            if num_r[square[i][j] - 1]:
                return 0
            if num_c[square[j][i] - 1]:
                return 0
            num_r[square[i][j] - 1] = 1
            num_c[square[j][i] - 1] = 1

            if i % 3 == 0 and j % 3 == 0:
                num = [0] * 9
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if num[square[r][c] - 1]:
                            return 0
                        num[square[r][c] - 1] = 1

    return 1


t = int(input())
for tc in range(1, t + 1):
    lst = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {sudoku(lst)}')

