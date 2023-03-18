import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find(num):
    if num != parents[num]:
        parents[num] = find(parents[num])
    return parents[num]


def union(x, y):
    global cycle
    x = find(x)
    y = find(y)
    if x != y:
        parents[min(x, y)] = max(x, y)


N, M = map(int, input().split())
parents = list(range(N))
cycle = 0

for i in range(M):
    a, b = map(int, input().split())
    if not cycle:
        if find(a) == find(b):
            cycle = i + 1
        else:
            union(a, b)
print(cycle)