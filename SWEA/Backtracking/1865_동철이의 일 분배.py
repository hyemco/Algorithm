def dfs(idx, total):
    global ans
    if total <= ans:
        return
    if idx == N:
        ans = total
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(idx + 1, total * work[idx][i]/100)
            visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    ans = 0
    dfs(0, 100)
    print(f'#{tc} {ans :.6f}')