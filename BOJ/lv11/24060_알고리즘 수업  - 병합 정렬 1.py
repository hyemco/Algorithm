def merge_s(li):
    if len(li) == 1:
        return li

    mid = (1 + len(li)) // 2
    left = merge_s(li[:mid])
    right = merge_s(li[mid:])

    tmp = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            ans.append(right[j])
            j += 1
    while i < len(left):
        tmp.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right):
        tmp.append(right[j])
        ans.append(right[j])
        j += 1
    return tmp


n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
merge_s(lst)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)