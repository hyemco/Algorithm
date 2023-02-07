for tc in range(1, 11):
    n = int(input())
    lst = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    di = [-1, 0, 0]
    dj = [0, -1, 1]

    for i in range(102):
        if lst[99][i] == 2:
            target_j = i
    k = 0
    last_i = 99
    while True:
        if last_i == 0:
            break
        if lst[last_i][target_j - 1]:
            k = 1
            while True:
                last_i += di[k]
                target_j += dj[k]
                if lst[last_i][target_j - 1] == 0:
                    break
        elif lst[last_i][target_j + 1]:
            k = 2
            while True:
                last_i += di[k]
                target_j += dj[k]
                if lst[last_i][target_j + 1] == 0:
                    break
        k = 0
        last_i += di[k]
        target_j += dj[k]
    print(f'#{tc} {target_j - 1}')