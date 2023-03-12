from collections import deque


def get_max_distance_node(node):
    global target_node
    max_d = 0
    visited = [False] * (V + 1)
    visited[node] = True
    Q = deque()
    Q.append((node, 0))

    while Q:
        now, now_d = Q.popleft()
        for c, c_d in adjL[now]:
            if not visited[c]:
                Q.append((c, now_d + c_d))
                visited[c] = True
                if max_d < now_d + c_d:
                    max_d = now_d + c_d
                    target_node = c
    return max_d


V = int(input())
if V == 1:
    print(0)
else:
    adjL = [[] for _ in range(V + 1)]
    for _ in range(V - 1):
        p, c, d = map(int, input().split())
        adjL[p].append((c, d))
        adjL[c].append((p, d))

    target_node = 0
    get_max_distance_node(1)
    ans = get_max_distance_node(target_node)
    print(ans)