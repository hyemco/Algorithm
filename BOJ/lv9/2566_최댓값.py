lst = []
max_n = -1
for i in range(9):
    lst.append(list(map(int, input().split())))
    for j in range(9):
        if max_n < lst[i][j]:
            max_n = lst[i][j]
            x = i + 1
            y = j + 1
print(max_n)
print(x, y)