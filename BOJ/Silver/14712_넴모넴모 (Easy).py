import sys
input = sys.stdin.readline


def solve(i, j):
    ans = 0
    if j > M:
        i, j = i + 1, 1
    if i > N:
        return 0
    if lst[i - 1][j] == 0 or lst[i][j - 1] == 0 or lst[i - 1][j - 1] == 0:
        lst[i][j] = 1
        ans += (1 + solve(i, j + 1))
        lst[i][j] = 0
    ans += solve(i, j + 1)

    return ans


N, M = map(int, input().rstrip().split())
lst = [[0] * (M + 1) for _ in range(N + 1)]
block_set = set()

print(solve(1, 1) + 1)