def distance(a, b):
    if a == 1:
        return b
    elif a == 2:
        return 2 * w + h - b
    elif a == 3:
        return 2 * (w + h) - b
    elif a == 4:
        return w + b


w, h = map(int, input().split())
N = int(input())
lst = []
ans = 0
for _ in range(N):
    d, length = map(int, input().split())
    lst.append(distance(d, length))

d, length = map(int, input().split())
t = distance(d, length)

for i in lst:
    route1 = abs(t - i)
    route2 = 2 * (w + h) - route1
    ans += min(route1, route2)

print(ans)