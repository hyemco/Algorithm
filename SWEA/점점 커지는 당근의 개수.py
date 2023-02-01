T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sizes = list(map(int, input().split()))

    cnt = 1
    cnt_lst = [1]
    for i in range(len(sizes) - 1):
        if sizes[i] < sizes[i + 1]:
            cnt += 1
            cnt_lst.append(cnt)
        else:
            cnt = 1
    print(f'#{test_case} {max(cnt_lst)}')