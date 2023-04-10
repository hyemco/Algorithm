import sys
input = sys.stdin.readline

N, K = map(int, input().split())
C = list(map(int, input().split()))

tubes = []

for i in enumerate(C, 1):
    tubes.append(i)

tubes.sort(key=lambda x: x[1])


if (N + 1) // 2 < tubes[-1][1]:
    print(-1)
else:
    tmp = []

    for idx, cnt in tubes:
        tmp += [idx] * cnt

    ans = [0] * N

    for i in range(0, N, 2):
        ans[i] = tmp.pop()

    for i in range(1, N, 2):
        ans[i] = tmp.pop()

    print(*ans)