N = int(input())

roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

ans = 0
m = costs[0]
for i in range(N - 1):
    if costs[i] < m:
        m = costs[i]
    ans += m * roads[i]

print(ans)