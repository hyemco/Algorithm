def paper(b):
    b //= 10
    f = [0] * (b + 2)
    f[1] = 1
    f[2] = 3
    for i in range(3, b + 1):
        f[i] = f[b - 1] + f[b - 2] * 2
    return f[b]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    print(f'#{tc} {paper(n)}')