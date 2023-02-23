def binary_tree(v):
    if v <= V:
        if not tree[v]:
            tree[v] = binary_tree(v * 2) + binary_tree(v * 2 + 1)
        return tree[v]
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    V, M, L = map(int, input().split())
    tree = [0] * (V + 1)

    for i in range(M):
        v, n = map(int, input().split())
        tree[v] = n
    binary_tree(1)
    print(f'#{tc} {tree[L]}')