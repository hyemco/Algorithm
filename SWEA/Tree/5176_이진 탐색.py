def binary_tree(n):
    global num
    if n <= N:
        binary_tree(n * 2)
        tree[n] = num
        num += 1
        binary_tree(n * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [i for i in range(N + 1)]
    num = 1
    binary_tree(1)

    print(f'#{tc} {tree[1]} {tree[N // 2]}')