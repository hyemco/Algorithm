T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    order = sorted(list(map(int, input().split())))

    rlt = 'Possible'
    for i in range(N):
        if (order[i] // M) * K < i + 1:
            rlt = 'Impossible'
    print(f'#{tc} {rlt}')