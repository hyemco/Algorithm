import sys

t = int(sys.stdin.readline())
lst = []
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a, b))

lst = sorted(lst, key=lambda x: (x[1], x[0]))

# 처음은 이렇게 품
# lst = sorted(sorted(lst, key=lambda x: x[0]), key=lambda x: x[1])
for i in lst:
    print(i[0], i[1])
