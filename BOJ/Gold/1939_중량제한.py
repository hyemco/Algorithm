# from collections import deque
import sys
input = sys.stdin.readline


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    parents[max(x, y)] = min(x, y)


N, M = map(int, input().split())
bridges = []
for _ in range(M):
    a, b, w = map(int, input().split())
    bridges.append([a, b, w])
t1, t2 = map(int, input().split())

bridges.sort(key=lambda x: -x[2])
parents = [i for i in range(N + 1)]

ans = 0
for u, v, w in bridges:
    parent_u = find_set(u)
    parent_v = find_set(v)
    if parent_u != parent_v:
        union(parent_u, parent_v)
        if find_set(t1) == find_set(t2):
            ans = w
            break
print(ans)



'''
bfs + 이분 탐색 방법
'''
# def bfs(weight):
#     Q = deque()
#     Q.append(target1)
#     visited = [False] * (N + 1)
#     visited[target1] = True
#
#     while Q:
#         now = Q.popleft()
#         if now == target2:
#             return True
#
#         for n, w in bridges[now]:
#             if not visited[n] and w >= weight:
#                 visited[n] = True
#                 Q.append(n)
#     return False
#
#
# N, M = map(int, input().split())
# bridges = [[] for _ in range(N + 1)]
#
# for _ in range(M):
#     a, b, w = map(int, input().split())
#     bridges[a].append([b, w])
#     bridges[b].append([a, w])
#
# target1, target2 = map(int, input().split())
#
# start, end = 1, 1000000000
#
# ans = 0
# while start <= end:
#     mid = (start + end) // 2
#
#     if bfs(mid):
#         ans = mid
#         start = mid + 1
#     else:
#         end = mid - 1
# print(ans)