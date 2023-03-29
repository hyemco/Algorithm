def merge_sort(lst):
    global cnt
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    idx = l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            lst[idx] = left[l]
            l += 1
        else:
            lst[idx] = right[r]
            r += 1
        idx += 1
    if l == len(left):
        for i in range(r, len(right)):
            lst[idx] = right[i]
            idx += 1
    elif r == len(right):
        cnt += 1
        for i in range(l, len(left)):
            lst[idx] = left[i]
            idx += 1
    return lst


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    in_lst = list(map(int, input().split()))
    cnt = 0

    ans = merge_sort(in_lst)[N // 2]
    print(f'#{tc} {ans} {cnt}')