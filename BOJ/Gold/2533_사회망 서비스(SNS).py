import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def is_child(node, parent):
    global cnt
    num_of_child = 0
    for link in graph[node]:
        if link != parent:
            num_of_child += is_child(link, node)

    if num_of_child:
        cnt += 1
        return 0
    else:
        return 1


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

is_child(1, 0)
print(cnt)