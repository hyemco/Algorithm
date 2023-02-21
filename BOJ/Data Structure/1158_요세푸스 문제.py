from collections import deque

N, K = map(int, input().split())

lst = deque([i for i in range(1, N + 1)])
ans = []

cnt = 0
while True:
    if len(ans) == N:
        break
    else:
        for i in range(K - 1):
            lst.append(lst.popleft())
        tmp = lst.popleft()
        ans.append(tmp)
s = ', '.join(map(str, ans))
print(f'<{s}>')