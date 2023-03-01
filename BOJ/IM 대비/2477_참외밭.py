K = int(input())
lst = []
for _ in range(6):
    d, length = map(int, input().split())
    lst.append(length)

max_1 = max([lst[i] for i in range(0, 6, 2)])
max_2 = max([lst[i] for i in range(1, 6, 2)])

min_1 = abs(lst[(lst.index(max_1) + 1) % 6] - lst[lst.index(max_1) - 1])
min_2 = abs(lst[(lst.index(max_2) + 1) % 6] - lst[lst.index(max_2) - 1])

ans = (max_1 * max_2 - min_1 * min_2) * K
print(ans)