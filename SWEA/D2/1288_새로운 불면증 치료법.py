T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = [False] * 10

    i = 1
    while False in num:
        tmp = N * i
        while tmp != 0:
            num[tmp % 10] = True
            tmp //= 10
        i += 1
    print(f'#{tc} {N * (i - 1)}')