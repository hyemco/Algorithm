T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    ans = 0
    delta = []
    for i in range(N // 2 + 1):
        for j in range(i - N // 2, N // 2 - i + 1):
            if i == 0:
                delta.append((i, j))
            else:
                delta.append((i, j))
                delta.append((-i, j))
    i = j = N // 2
    for d in delta:
        ni, nj = i + d[0], j + d[1]
        ans += farm[ni][nj]
    print(f'#{tc} {ans}')