import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    Q = deque()
    Q.append((A, ''))
    visited = [False] * 10000
    visited[A] = True

    while Q:
        num, cmd = Q.popleft()

        if num == B:
            print(cmd)
            break

        D = (num * 2) % 10000
        if not visited[D]:
            visited[D] = True
            Q.append((D, cmd + 'D'))

        S = (num - 1) % 10000
        if not visited[S]:
            visited[S] = True
            Q.append((S, cmd + 'S'))

        L = (num % 1000) * 10 + (num // 1000)
        if not visited[L]:
            visited[L] = True
            Q.append((L, cmd + 'L'))

        R = (num % 10) * 1000 + (num // 10)
        if not visited[R]:
            visited[R] = True
            Q.append((R, cmd + 'R'))