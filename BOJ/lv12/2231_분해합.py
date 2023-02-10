n = int(input())

r = len(str(n)) * 9

if n - r < 0:
    s = 1
else:
    s = n - r
for i in range(s, n + 1):
    a = list(map(int, str(i)))
    sub_sum = i + sum(a)
    if sub_sum == n:
        print(i)
        break
    elif i == n:
        print(0)