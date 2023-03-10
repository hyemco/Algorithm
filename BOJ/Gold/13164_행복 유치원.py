import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kids = list(map(int, input().split()))

diff = []
for i in range(N - 1):
    diff.append(kids[i + 1] - kids[i])

diff.sort(reverse=True)
ans = sum(diff[K - 1:])
print(ans)