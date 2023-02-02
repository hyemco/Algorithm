T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    lst.append(0)
    cnt_lst = []
    cnt = 1
    for i in range(0, N):
        if lst[i] == lst[i + 1] == 1:
            cnt += 1
        else:
            cnt_lst.append(cnt)
            cnt = 1
    print(f'#{test_case} {max(cnt_lst)}')