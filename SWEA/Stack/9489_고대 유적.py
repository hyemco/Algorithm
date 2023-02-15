
def dfs(x, y, v, cnt):
    global ans
    if not lst[x][y]:
        return
    if m > y + 1 >= 0 == v:
        if lst[x][y + 1]:
            dfs(x, y + 1, 0, cnt + 1)
    if 0 <= x + 1 < n and v == 1:
        if lst[x + 1][y]:
            dfs(x + 1, y, 1, cnt + 1)
    if ans < cnt:
        ans = cnt


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    cnt, ans = 1, 0
    for i in range(n):
        for j in range(m):
            if lst[i][j]:
                dfs(i, j, 0, cnt)
                dfs(i, j, 1, cnt)
    print(f'#{tc} {ans} ')