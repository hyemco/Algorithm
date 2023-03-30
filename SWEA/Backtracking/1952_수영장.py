def dfs(idx, total):
    global ans
    if ans <= total:
        return

    if idx > 11:
        ans = min(ans, total)
        return

    dfs(idx + 1, total + (day * plans[idx]))
    dfs(idx + 1, total + month)
    dfs(idx + 3, total + three_month)
    dfs(idx + 12, total + year)


T = int(input())
for tc in range(1, T + 1):
    day, month, three_month, year = map(int, input().split())
    plans = list(map(int, input().split()))

    ans = year
    dfs(0, 0)
    print(f'#{tc} {ans}')