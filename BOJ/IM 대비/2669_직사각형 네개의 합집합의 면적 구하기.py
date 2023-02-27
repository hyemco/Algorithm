lst = [[0] * 101 for _ in range(101)]
for _ in range(4):
    i1, j1, i2, j2 = map(int, input().split())

    for i in range(i1, i2):
        for j in range(j1, j2):
            if lst[i][j] == 0:
                lst[i][j] = 1

ans = 0
for i in lst:
    ans += i.count(1)
print(ans)