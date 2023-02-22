T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    service = []

    for k in range(1, N + 2):
        cost = k ** 2 + (k - 1) ** 2

        for i in range(k):
            for j in range(-k + 1 + i, k - i):
                if i == 0:
                    service.append((i, j))
                else:
                    service.append((i, j))
                    service.append((-i, j))
        service = list(set(service))

        for i in range(N):
            for j in range(N):
                cnt = 0
                for s in service:
                    ni, nj = i + s[0], j + s[1]
                    if 0 <= ni < N and 0 <= nj < N:
                        if city[ni][nj] == 1:
                            cnt += 1
                if M * cnt >= cost:
                    if cnt > ans:
                        ans = cnt
    print(f'#{tc} {ans}')
