def dfs():
    if len(tmp) == M:
        for i in range(M):
            print(tmp[i], end=' ')
        print('')
        return
    for i in range(0, N):
        if graph[i] in tmp:
            continue

        tmp.append(graph[i])
        dfs()
        tmp.pop()


N, M = map(int, input().split())
graph = list(map(int, input().split()))

tmp = []

graph.sort()
dfs()