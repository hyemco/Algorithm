from collections import deque


def bfs(a, b):
    Q = deque([(a, 1)])

    while Q:
        now, cnt = Q.popleft()
        if now == b:
            print(cnt)
            return

        if now * 2 <= b:
            Q.append((now * 2, cnt + 1))
        if now * 10 + 1 <= b:
            Q.append((now * 10 + 1, cnt + 1))
    print(-1)


A, B = map(int, input().split())
bfs(A, B)