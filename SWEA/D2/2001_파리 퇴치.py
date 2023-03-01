T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_V = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for y in range(i, i + M):
                for x in range(j, j + M):
                    cnt += lst[y][x]
            if cnt > max_V:
                max_V = cnt

    print(f'#{tc} {max_V}')