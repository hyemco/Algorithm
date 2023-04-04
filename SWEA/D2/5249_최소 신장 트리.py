def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    rep = [i for i in range(V + 1)]
    edge = []
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        edge.append([v1, v2, w])
    edge.sort(key=lambda x: x[2])

    ans = cnt = 0
    for a, b, w in edge:
        rep_a = find_set(a)
        rep_b = find_set(b)
        if rep_a != rep_b:
            cnt += 1
            ans += w
            rep[rep_b] = rep_a
            if cnt == V:
                break
    print(f'#{tc} {ans}')