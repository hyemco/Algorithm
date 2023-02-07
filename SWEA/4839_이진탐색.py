def binary_search(page, target):
    start = 1
    end = page
    cnt = 1
    while start <= end:
        mid = (start + end) // 2
        if mid == target or start == target or end == target:
            return cnt
        elif mid > target:
            end = mid
            cnt += 1
        else:
            start = mid
            cnt += 1


T = int(input())
for test_case in range(1, T + 1):
    p, a, b = map(int, input().split())
    p1 = binary_search(p, a)
    p2 = binary_search(p, b)
    if p1 == p2:
        winner = 0
    elif p1 < p2:
        winner = 'A'
    else:
        winner = 'B'
    print(f'#{test_case} {winner}')