def paper(N):
    n = N // 10
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 3
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2] * 2
    return f[n]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    print(f'#{tc} {paper(n)}')