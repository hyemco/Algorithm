import sys

t = int(sys.stdin.readline())
lst = [0] * 10

for _ in range(t):
    lst[int(sys.stdin.readline())] += 1

for i in range(10):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)