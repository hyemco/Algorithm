t = int(input())

base = [[0] * 100 for _ in range(100)]
for _ in range(t):
    x, y = map(int, input().split())
    for i in range(y - 1, y + 9):
        for j in range(x - 1, x + 9):
            base[i][j] = 1
cnt = []
for i in base:
    cnt.append(i.count(1))
print(sum(cnt))