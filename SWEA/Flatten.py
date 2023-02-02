for test_case in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N):
        min_idx = lst.index(min(lst))
        max_idx = lst.index(max(lst))
        lst[min_idx] += 1
        lst[max_idx] -= 1

    ans = max(lst) - min(lst)
    print(f'#{test_case} {ans}')