N = int(input())
lst = [[0] * 1001 for _ in range(1001)]
for k in range(N):
    x, y, w, h = map(int, input().split())
    for i in range(y, y + h):
        lst[i][x:x + w] = [k + 1] * w

for k in range(N):
    cnt = 0
    for l in lst:
        cnt += l.count(k + 1)
    print(cnt)