N = int(input())
lst = [[0] * 100 for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        lst[i][x:x + 10] = [1] * 10

ans = 0
for l in lst:
    ans += l.count(1)
print(ans)