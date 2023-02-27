T = int(input())
for tc in range(1, T + 1):
    letters = [list(input()) for _ in range(5)]

    print(f'#{tc}', end=' ')
    for i in range(15):
        for j in range(5):
            try:
                print(letters[j][i], end='')
            except IndexError:
                pass
    print()