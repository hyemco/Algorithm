T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [0] + list(map(int, input().split()))
    ans = 0

    for i in range(1, N + 1):
        while V[i // 2] > V[i]:
            V[i // 2], V[i] = V[i], V[i // 2]
            i //= 2

    p = N // 2
    while p > 0:
        ans += V[p]
        p //= 2
    print(f'#{tc} {ans}')