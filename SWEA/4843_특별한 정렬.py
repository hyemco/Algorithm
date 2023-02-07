t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n):
        min_idx = i
        if i % 2:
            for j in range(i + 1, n):
                if lst[min_idx] > lst[j]:
                    min_idx = j
        else:
            for j in range(i + 1, n):
                if lst[min_idx] < lst[j]:
                    min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print(f'#{tc}', *lst[:10])