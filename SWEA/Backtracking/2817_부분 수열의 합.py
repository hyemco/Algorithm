def bfs(idx, total):
    global ans
    if idx == N:
        if total == K:
            ans += 1
        return
    bfs(idx + 1, total + numbers[idx])
    bfs(idx + 1, total)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    ans = 0
    bfs(0, 0)
    print(f'#{tc} {ans}')