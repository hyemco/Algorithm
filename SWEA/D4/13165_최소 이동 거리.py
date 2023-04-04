T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    INF = 10 * 8
    graph = [[INF] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    D = [INF] * (V + 1)
    D[0] = 0

    for i in range(V + 1):
        for j in range(V + 1):
            if i != j and graph[i][j] != INF:
                if D[i] + graph[i][j] < D[j]:
                    D[j] = D[i] + graph[i][j]
    ans = D[-1]
    print(f'#{tc} {ans}')
