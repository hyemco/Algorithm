def subtree(V):
    global cnt
    if V == 0:
        return
    cnt += 1
    subtree(left[V])
    subtree(right[V])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    inp = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(len(inp) // 2):
        p, c = inp[i * 2], inp[i * 2 + 1]
        if not left[p]:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    subtree(N)
    print(f'#{tc} {cnt}')