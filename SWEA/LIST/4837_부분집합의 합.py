T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())    # n:원소의 수, k:집합 합
    origin_set = list(range(1, 13))
    cnt = 0

    for i in range(1 << 12):
        subset = []
        total = 0
        for j in range(12):
            if i & (1 << j):
                subset.append(origin_set[j])
        if sum(subset) == k and len(subset) == n:
            cnt += 1
    print(f'#{test_case} {cnt}')