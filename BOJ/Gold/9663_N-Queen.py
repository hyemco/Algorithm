def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queen(x):
    global ans
    if x == N:
        ans += 1
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                n_queen(x + 1)


N = int(input())
row = [0] * N
ans = 0

n_queen(0)
print(ans)
