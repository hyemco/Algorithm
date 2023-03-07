def select_chicken(cnt):
    if cnt == M:
        tmp = 0
        for i, j in home:
            d = (N * M) ** 2
            for e, (ci, cj) in tmp_chicken:
                d = min(d, abs(i - ci) + abs(j - cj))
            tmp += d
        rlt.append(tmp)

    for e, (ci, cj) in enumerate(chicken):
        if visited[ci][cj] == 0:
            if tmp_chicken:
                if e < tmp_chicken[-1][0]:
                    continue

            visited[ci][cj] = 1
            tmp_chicken.append((e, (ci, cj)))
            select_chicken(cnt + 1)
            visited[ci][cj] = 0
            tmp_chicken.pop()


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
tmp_chicken = []
rlt = []
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

select_chicken(0)
print(min(rlt))