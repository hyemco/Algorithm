T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrot = sorted(list(map(int, input().split())))

    ans = 1000
    for i in range(N - 2):
        if carrot[i] != carrot[i + 1]:
            for j in range(i + 1, N - 1):
                if carrot[j] != carrot[j + 1]:
                    A = i + 1
                    B = j - i
                    C = N - 1 - j
                    if A * B * C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:
                        ans = min(ans, max(A, B, C) - min(A, B, C))
    if ans == 1000:
        ans = -1
    print(f'#{tc} {ans}')