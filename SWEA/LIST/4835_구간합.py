T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    temp_lst = []
    n = 0
    temp_sum = 0
    for _ in range(N - M + 1):
        for i in range(n, n + M):
            temp_sum += lst[i]
        temp_lst.append(temp_sum)
        temp_sum = 0
        n += 1
    print(f'#{test_case} {max(temp_lst) - min(temp_lst)}')