n = - 1
while n != 0:
    n = int(input())
    ans = [True] * ((2 * n) + 1)
    cnt = []
    for i in range(2, round((2 * n) ** 0.5) + 1):
        if ans[i]:
            mul = 2
            while i * mul <= 2 * n:
                ans[i * mul] = False
                mul += 1
    for i in range(n + 1, (2 * n) + 1):
        if ans[i]:
            cnt.append(i)
    if n != 0:
        print(len(cnt))