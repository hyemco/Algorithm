import sys
from collections import deque
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
in_degree = [0] * (V + 1)
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    in_degree[e] += 1

Q = deque()
ans = [0] * (V + 1)
for i in range(1, V + 1):
    if in_degree[i] == 0:
        Q.append(i)
        ans[i] = 1

while Q:
    now = Q.popleft()
    for i in graph[now]:
        idx = i[0]
        if i[1] < 7:
            ans[idx] = max(ans[idx], ans[now] + i[1])
        else:
            ans[idx] = max(ans[idx], ans[now] + i[1] + 1)

        in_degree[idx] -= 1
        if in_degree[idx] == 0:
            Q.append(idx)

print(max(ans))