T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    ans = [0] * 5
    div_lst = [2, 3, 5, 7, 11]
    i = 0
    while n > 1:
        if n % div_lst[i] == 0:
            idx = div_lst.index(div_lst[i])
            ans[idx] += 1
            n //= div_lst[i]
        else:
            i += 1

    print(f'#{test_case}', *ans)