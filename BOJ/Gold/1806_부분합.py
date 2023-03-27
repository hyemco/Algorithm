import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

left = right = 0
target = 0
ans = sys.maxsize

while True:
    if target >= S:
        target -= lst[left]
        ans = min(ans, right - left)
        left += 1
    else:
        if right == N:
            break
        target += lst[right]
        right += 1

if ans == sys.maxsize:
    print(0)
else:
    print(ans)