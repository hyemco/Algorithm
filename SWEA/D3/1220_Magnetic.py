T = 10
for tc in range(1, T + 1):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    turn_magnetic = list(map(list, zip(*magnetic)))

    ans = 0
    for m in turn_magnetic:
        m = [i for i in m if i != 0]
        for j in range(len(m) - 1):
            if m[j] == 1 and m[j + 1] == 2:
                ans += 1
    print(f'#{tc} {ans}')