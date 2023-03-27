def battery(x, y, total):
    global ans
    if total > ans:
        return
    if x == N:
        total += golf[y][0]
        if total < ans:
            ans = total
            return
    for i in range(1, N):
        if not golf[y][i]:
            continue
        if not visited[i]:
            visited[i] = 1
            battery(x + 1, i, total + golf[y][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    golf = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]

    ans = 100 * N
    battery(1, 0, 0)
    print(f'#{tc} {ans}')
