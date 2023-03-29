def partition(lst, left, right):
    pivot = lst[left]
    i = left
    j = right

    while i <= j:
        while i <= j and pivot >= lst[i]:
            i += 1
        while i <= j and pivot <= lst[j]:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[left], lst[j] = lst[j], lst[left]
    return j


def quick_sort(lst, left, right):
    if left < right:
        pivot_idx = partition(lst, left, right)
        quick_sort(lst, left, pivot_idx - 1)
        quick_sort(lst, pivot_idx + 1, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, N - 1)

    ans = numbers[N // 2]
    print(f'#{tc} {ans}')