t = int(input())
for tc in range(1, t + 1):
    day = int(input())
    lst = list(map(int, input().split()))
    max_v = lst[-1]
    ans = 0
    for i in range(day - 2, -1, -1):
        if lst[i] >= max_v:
            max_v = lst[i]
        else:
            ans += max_v - lst[i]

    print(f'#{tc} {ans}')