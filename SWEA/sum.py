for _ in range(1, 11):
    tc = int(input())
    lst = []
    sum_lst = []
    for _ in range(100):
        l = list(map(int, input().split()))
        lst.append(l)
        sum_lst.append(sum(l))
    sum_n1 = sum_n2 = 0
    for i in range(100):
        sum_n1 += lst[i][i] # 왼위-오아 대각선
        sum_n2 += lst[i][99 - i]    # 오위 - 왼아 대각선
        sum_n3 = 0
        for j in range(100):
            sum_n3 += lst[j][i]
        sum_lst.append(sum_n3)
    sum_lst.append(sum_n1)
    sum_lst.append(sum_n2)
    print(f'#{tc} {max(sum_lst)}')