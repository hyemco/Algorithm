T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0] * len(money)

    for i in range(len(money)):
        if N >= money[i]:
            ans[i] = N // money[i]
            N -= (N // money[i]) * money[i]
    print(f'#{tc}')
    print(*ans)