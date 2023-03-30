def dfs(idx, score, cal):
    global ans
    if cal > L:
        return
    if score > ans:
        ans = score
    if idx == N:
        return
    dfs(idx + 1, score + ingredients[idx][0], cal + ingredients[idx][1])
    dfs(idx + 1, score, cal)


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')
