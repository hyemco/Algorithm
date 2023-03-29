def binary_search(t):
    global ans
    left = 0
    right = N - 1

    flag = 0
    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == t:
            ans += 1
            return
        elif t < numbers[mid]:
            if flag == 1:
                break
            right = mid - 1
            flag = 1
        else:
            if flag == 2:
                break
            left = mid + 1
            flag = 2


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    targets = list(map(int, input().split()))

    ans = 0
    for target in targets:
        binary_search(target)

    print(f'#{tc} {ans}')