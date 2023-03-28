T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x: x[1])

    ans = end = 0
    for time in times:
        if time[0] >= end:
            ans += 1
            end = time[1]
    print(f'#{tc} {ans}')