from collections import deque


def bfs(start, end):
    visited = [0] * (V + 1)
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in lst[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1
                if i == end:
                    return visited[i] - 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V + 1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        lst[v1].append(v2)
        lst[v2].append(v1)

    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, G)}')