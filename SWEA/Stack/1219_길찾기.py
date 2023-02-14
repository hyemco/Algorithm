for _ in range(10):
    tc, E = map(int, input().split())
    lst = [[] for _ in range(100)]
    inp = list(map(int, input().split()))

    for i in range(E):
        v1, v2 = inp[i * 2], inp[i * 2 + 1]
        lst[v1].append(v2)

    visited = [False] * 100
    stack = [0]
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            for v in lst[now]:
                if not visited[v]:
                    stack.append(v)
    if visited[99]:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')