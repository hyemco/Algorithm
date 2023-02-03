import sys

t = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(t)]
for i in sorted(lst):
    print(i)