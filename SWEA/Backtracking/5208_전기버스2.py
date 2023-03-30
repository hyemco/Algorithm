def backtracking(n, cnt, total):
    global ans
    if ans <= cnt:
        return
    if n == station - 1:
        ans = min(ans, cnt)
        return
    if total > 0:
        backtracking(n + 1, cnt, total - 1)
    backtracking(n + 1, cnt + 1, battery[n] - 1)


T = int(input())
for tc in range(1, T + 1):
    battery = list(map(int, input().split()))
    station = battery.pop(0)

    ans = station
    backtracking(1, 0, battery[0] - 1)
    print(f'#{tc} {ans}')