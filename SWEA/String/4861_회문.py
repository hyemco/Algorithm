t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    lst = [input() for _ in range(n)]

    for i in range(n):
        for j in range(n - m + 1):
            if lst[i][j:j + m] == lst[i][j:j + m][::-1]:
                print(f'#{tc} {lst[i][j:j + m]}')
                break

    for i in range(n - m + 1):
        for j in range(n):
            c_lst = []
            for r in range(m):
                c_lst.append(lst[i + r][j])
            if c_lst == c_lst[::-1]:
                print(f'#{tc} ', *c_lst, sep='')
                break
