from collections import deque


def bfs(start, end):
    Q.append(start)
    visited[start] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                distance[w] = distance[v] + 1
                Q.append(w)
                if w == end:
                    return distance[w]
    return 0


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    start, end = map(int, input().split())
    visited = [0] * (V + 1)
    distance = [0] * (V + 1)
    Q = deque()
    print(f'#{tc} {bfs(start, end)}')