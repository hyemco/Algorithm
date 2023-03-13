import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
route = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    route[a].append((c, b))
    route[b].append((c, a))
total_cost = [sys.maxsize for _ in range(V + 1)]


def dijkstra():
    Q = []
    heapq.heappush(Q, (0, 1))
    total_cost[1] = 0

    while Q:
        cost, now = heapq.heappop(Q)
        if now == V:
            return total_cost[now]
        if total_cost[now] < cost:
            continue
        for n_c, n_v in route[now]:
            if cost + n_c < total_cost[n_v]:
                total_cost[n_v] = cost + n_c
                heapq.heappush(Q, (cost + n_c, n_v))


print(dijkstra())
