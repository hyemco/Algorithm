import sys
input = sys.stdin.readline
t = int(input())
lst = []
for _ in range(t):
    a, n = input().split()
    lst.append((a, n))

lst = sorted(lst, key=lambda x: int(x[0]))
for i in lst:
    print(i[0], i[1])