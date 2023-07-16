from collections import deque

N = int(input())
Q = deque(enumerate(map(int, input().split())))

ans = []
while Q:
    idx, target = Q.popleft()
    ans.append(idx + 1)

    if target > 0:
        Q.rotate(-(target - 1))
    elif target < 0:
        Q.rotate(-target)

for i in ans:
    print(i, end=' ')