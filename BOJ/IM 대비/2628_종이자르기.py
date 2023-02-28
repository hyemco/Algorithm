W, H = map(int, input().split())
N = int(input())

y = [(0, H)]
x = [(0, W)]
for _ in range(N):
    d, idx = map(int, input().split())
    if d == 0:
        for i in y:
            if idx in range(i[0], i[1]):
                y.append((i[0], idx))
                y.append((idx, i[1]))
                y.remove(i)
                break

    if d == 1:
        for i in x:
            if idx in range(i[0], i[1]):
                x.append((i[0], idx))
                x.append((idx, i[1]))
                x.remove(i)
                break

y = [b - a for a, b in y]
x = [b - a for a, b in x]

ans = max(y) * max(x)
print(ans)