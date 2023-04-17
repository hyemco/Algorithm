import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N + 1)
orders = [[] for _ in range(N+1)]

for _ in range(M):
    tmp = list(map(int, input().split()))[1:]
    for i in range(len(tmp) - 1):
        orders[tmp[i]].append(tmp[i + 1])
        indegree[tmp[i + 1]] += 1

Q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        Q.append(i)

ans = []
while Q:
    num = Q.popleft()
    ans.append(num)
    for order in orders[num]:
        indegree[order] -= 1
        if indegree[order] == 0:
            Q.append(order)

if len(ans) != N:
    print(0)
else:
    print(*ans, sep='\n')