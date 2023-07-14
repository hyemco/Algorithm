def dfs(x, y):
    if graph[x][y] == '-':
        graph[x][y] = 1
        for k in [1, -1]:
            ny = y + k
            if (-1 < ny < M) and graph[x][ny] == '-':
                dfs(x, ny)
    elif graph[x][y] == '|':
        graph[x][y] = 1
        for k in [1, - 1]:
            nx = x + k
            if (-1 < nx < N) and graph[nx][y] == '|':
                dfs(nx, y)


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(input()))

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            cnt += 1

print(cnt)