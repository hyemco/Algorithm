t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    sum_lst = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sum_n = 0
            for x in range(i, i + m):
                for y in range(j, j + m):
                    sum_n += lst[x][y]
            sum_lst.append(sum_n)
    print(f'#{tc} {max(sum_lst)}')
