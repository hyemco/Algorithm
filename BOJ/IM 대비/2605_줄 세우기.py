N = int(input())
line = [0] * N
a = [0] * N
order = list(map(int, input().split()))
for i in range(N):
    line.insert(i - order[i], i + 1)
    a[i - order[i]] = i + 1

order = [i for i in line if i != 0]
print(*order)