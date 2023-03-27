import sys
from collections import deque
input = sys.stdin.readline


def get_distance(node):
    distance = [0] + [-1] * N
    Q = deque([(node, 0)])
    distance[node] = 0
    while Q:
        v, d = Q.popleft()
        for building in buildings[v]:
            if distance[building] == -1:
                distance[building] = d + 1
                Q.append((building, d + 1))

    return distance


N, M = map(int, input().split())
buildings = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    buildings[a].append(b)
    buildings[b].append(a)

tmp = [[0]]
for i in range(1, N + 1):
    tmp.append(get_distance(i))

ans = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        total = sum(map(min, zip(tmp[i], tmp[j])))
        ans.append((i, j, total))
ans.sort(key=lambda x: x[2])
print(ans[0][0], ans[0][1], ans[0][2] * 2)