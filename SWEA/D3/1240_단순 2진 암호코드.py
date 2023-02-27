def change_num(lst):
    if lst == [0, 0, 0, 1, 1, 0, 1]:
        return 0
    elif lst == [0, 0, 1, 1, 0, 0, 1]:
        return 1
    elif lst == [0, 0, 1, 0, 0, 1, 1]:
        return 2
    elif lst == [0, 1, 1, 1, 1, 0, 1]:
        return 3
    elif lst == [0, 1, 0, 0, 0, 1, 1]:
        return 4
    elif lst ==[0, 1, 1, 0, 0, 0, 1]:
        return 5
    elif lst == [0, 1, 0, 1, 1, 1, 1]:
        return 6
    elif lst == [0, 1, 1, 1, 0, 1, 1]:
        return 7
    elif lst == [0, 1, 1, 0, 1, 1, 1]:
        return 8
    elif lst == [0, 0, 0, 1, 0, 1, 1]:
        return 9


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pw = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(M - 1, -1, -1):
            if pw[i][j] == 1:
                idx = i
                end = j + 1
                break
        else:
            continue
        break

    num = []
    for j in range(end - 56, end, 7):
        num.append(change_num(pw[idx][j:j+7]))
    odd_sum, even_sum = 0, 0
    for i in range(len(num) // 2):
        odd_sum += num[i * 2]
        even_sum += num[i * 2 + 1]

    if (odd_sum * 3 + even_sum) % 10 == 0:
        print(f'#{tc} {odd_sum + even_sum}')
    else:
        print(f'#{tc} 0')