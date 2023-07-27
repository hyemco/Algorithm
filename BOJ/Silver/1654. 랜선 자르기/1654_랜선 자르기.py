import sys

input = sys.stdin.readline


def solution():
    K, N = map(int, input().split())

    lan = [int(input()) for _ in range(K)]

    min_lan = 1
    max_lan = max(lan)

    while min_lan <= max_lan:
        mid = (min_lan + max_lan) // 2
        cnt = 0

        for i in lan:
            cnt += (i // mid)

        if cnt >= N:
            min_lan = mid + 1
        else:
            max_lan = mid - 1

    return max_lan


ans = solution()
print(ans)