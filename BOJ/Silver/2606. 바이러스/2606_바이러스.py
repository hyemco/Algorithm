N = int(input())
k = int(input())

graph = [[] for i in range(N + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)


def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)


dfs(1)
ans = sum(visited) - 1  # 1번 컴퓨터 제외
print(ans)