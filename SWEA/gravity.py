T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    box_lst = list(map(int, input().split()))

    max_n = 0
    for i in range(N):
        cnt = 0
        for j in range(i + 1, N):
            if box_lst[i] > box_lst[j]:
                cnt += 1
        if max_n < cnt:
            max_n = cnt

    print(f'#{test_case} {max_n}')