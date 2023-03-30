def backtracking(idx, total):
    global ans
    if ans < total:
        return
    if idx == N:
        ans = min(ans, total)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(idx + 1, total + factories[idx][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    factories = [list(map(int, input().split())) for _ in range(N)]

    ans = 100 * N
    visited = [0] * N

    backtracking(0, 0)
    print(f'#{tc} {ans}')