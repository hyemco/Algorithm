t = int(input())
lst = []
for _ in range(t):
    a, b = map(int, input().split())
    lst.append((a, b))
lst = sorted(lst)
for i in lst:
    print(i[0], i[1])