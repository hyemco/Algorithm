for tc in range(1, 11):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    result_cnt = 10000000
    for n in range(100):
        if lst[0][n] == 1:
            cnt = 0
            x, y = n, 0
            while 1:
                if x < 99 and lst[y][x+1]:
                    while x < 99 and lst[y][x+1]:
                        x += 1
                        cnt += 1
                    else:
                        y += 1
                elif x > 0 and lst[y][x-1]:
                    while x > 0 and lst[y][x-1]:
                        x -= 1
                        cnt += 1
                    else:
                        y += 1

                elif lst[y+1][x] == 1:
                    y += 1
                if y == 99:
                    if result_cnt >= cnt:
                        result_cnt = cnt
                        result = n
                    break
    print(f'#{tc} {result}')