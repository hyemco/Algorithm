T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    delta1 = []
    delta2 = []
    for i in range(M):
        if i == 0:
            for j in range(-M + 1, M):
                delta1.append((i, j))
            delta2.append((i, 0))
        else:
            delta1.append((i, 0))
            delta1.append((-i, 0))
            delta2.append((i, i))
            delta2.append((-i, i))
            delta2.append((i, -i))
            delta2.append((-i, -i))

    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for d in delta1:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < N and 0 <= nj < N:
                    cnt += fly[ni][nj]
            ans = max(ans, cnt)
            cnt = 0
            for d in delta2:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < N and 0 <= nj < N:
                    cnt += fly[ni][nj]
            ans = max(ans, cnt)
    print(f'#{tc} {ans}')