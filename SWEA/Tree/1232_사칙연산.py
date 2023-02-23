def postorder(node):
    if node:
        postorder(left[node])
        postorder(right[node])
        if tree[node] == '+':
            tree[node] = tree[left[node]] + tree[right[node]]
        elif tree[node] == '-':
            tree[node] = tree[left[node]] - tree[right[node]]
        elif tree[node] == '*':
            tree[node] = tree[left[node]] * tree[right[node]]
        elif tree[node] == '/':
            tree[node] = tree[left[node]] // tree[right[node]]
    return


T = 10
for tc in range(1, T + 1):
    V = int(input())
    tree = [0] * (V + 1)
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for _ in range(V):
        inp = input().split()
        try:
            tree[int(inp[0])] = int(inp[1])
        except ValueError:
            tree[int(inp[0])] = inp[1]
            left[int(inp[0])] = int(inp[2])
            right[int(inp[0])] = int(inp[3])
    postorder(1)
    ans = tree[1]
    print(f'#{tc} {ans}')