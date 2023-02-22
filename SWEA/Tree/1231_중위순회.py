def binary_tree(n):
    if n:
        left_n = binary_tree(left[n])
        right_n = binary_tree(right[n])
        return str(left_n) + tree[n] + str(right_n)
    else:
        return ""


for tc in range(1, 11):
    V = int(input())
    tree = [0] * (V + 1)
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for _ in range(V):
        inp = input().split()
        tree[int(inp[0])] = inp[1]
        try:
            left[int(inp[0])] = int(inp[2])
            right[int(inp[0])] = int(inp[3])

        except IndexError:
            pass
    ans = binary_tree(1)
    print(f'#{tc} {ans}')


