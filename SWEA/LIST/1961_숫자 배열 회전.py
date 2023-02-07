def rotate(li):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = li[n - 1 - j][i]
    return tmp


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    lst1 = rotate(lst)
    lst2 = rotate(lst1)
    lst3 = rotate(lst2)

    print(f'#{tc }')
    for a, b, c in zip(lst1, lst2, lst3):
        print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str,c))}')

    # 아래 코드를 zip, join으로 변경
    # for i in range(n):
    #     for j in range(n):
    #         print(lst1[i][j], end='')
    #     print(end=' ')
    #     for j in range(n):
    #         print(lst2[i][j], end='')
    #     print(end=' ')
    #     for j in range(n):
    #         print(lst3[i][j], end='')
    #     print()