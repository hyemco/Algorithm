def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queen(i):
    global ans
    if i == N:
        ans += 1
    else:
        for j in range(N):
            row[i] = j
            if check(i):
                n_queen(i + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    row = [0] * N
    ans = 0

    n_queen(0)
    print(f'#{tc} {ans}')
