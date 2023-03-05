from collections import deque

gear = [deque(list(map(int, input()))) for _ in range(4)]


def left_side(idx, dirs):
    if idx < 0 or gear[idx][2] == gear[idx + 1][6]:
        return
    elif gear[idx][2] != gear[idx + 1][6]:
        left_side(idx - 1, -dirs)
        gear[idx].rotate(-dirs)


def right_side(idx, dirs):
    if idx > 3 or gear[idx][6] == gear[idx - 1][2]:
        return
    elif gear[idx][6] != gear[idx - 1][2]:
        right_side(idx + 1, -dirs)
        gear[idx].rotate(-dirs)


K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    n -= 1
    left_side(n - 1, d)
    right_side(n + 1, d)
    gear[n].rotate(d)

ans = 0
for i in range(4):
    if gear[i][0] == 1:
        ans += 2 ** i
print(ans)