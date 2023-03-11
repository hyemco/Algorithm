from collections import deque


def bfs(idx):
    tmp = 0
    Q = deque([idx])
    visited[idx] = True

    while Q:
        for q in Q:
            teams[tmp].append(q)
        for _ in range(len(Q)):
            v = Q.popleft()
            for adj in adjL[v]:
                if not visited[adj]:
                    visited[adj] = True
                    Q.append(adj)
        tmp += 1
        if tmp % 2:
            tmp = 0


N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

adjL = [[] for _ in range(N + 1)]
for i in range(N):
    for j in info[i][1:]:
        adjL[i + 1].append(j)

teams = [[], []]
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)

for i in range(2):
    print(teams[i])