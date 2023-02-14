t = int(input())
for tc in range(1, t + 1):
    V, E = map(int, input().split())
    lst = [[0] * (V + 1) for _ in range(V + 1)]
    ans = 0
    for _ in range(E):
        v1, v2 = map(int, input().split())
        lst[v1][v2] = 1
    start, end = map(int, input().split())

    stack = []
    visit = [False] * (V + 1)
    stack.append(start)
    while stack:
        v = stack.pop()
        visit[v] = True
        for p in range(V + 1):
            if not visit[p]:
                if lst[v][p]:
                    stack.append(p)
    if visit[end]:
        ans = 1
    print(f'#{tc} {ans}')