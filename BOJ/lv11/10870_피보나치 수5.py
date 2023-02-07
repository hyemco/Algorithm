n = int(input())
lst = [0, 1]
for i in range(n - 1):
    lst.append(lst[i] + lst[i + 1])
print(lst[n])