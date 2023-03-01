T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    ans = 0

    min_cnt = N * M
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            cnt = 0
            for k in range(i + 1):
                cnt += M - flag[k].count('W')
            for k in range(i + 1, j + 1):
                cnt += M - flag[k].count('B')
            for k in range(j + 1, N):
                cnt += M - flag[k].count('R')

            min_cnt = min(min_cnt, cnt)
    ans += min_cnt
    print(f'#{tc} {ans}')