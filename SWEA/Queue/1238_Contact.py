from collections import deque


def bfs():
    visited = [0] * 101
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in adjL[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1
    return [n for n, ele in enumerate(visited) if ele == max(visited)]


for tc in range(1, 11):
    data_len, start = map(int, input().split())
    contact_N = list(map(int, input().split()))
    adjL = [[] for _ in range(101)]

    for i in range(data_len // 2):
        f, t = i * 2, i * 2 + 1
        adjL[contact_N[f]].append(contact_N[t])

    ans = max(bfs())
    print(f'#{tc} {ans}')