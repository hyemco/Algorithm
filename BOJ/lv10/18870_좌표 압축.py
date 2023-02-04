import sys

t = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
de_lst = sorted(list(set(lst)))
n_dict = {de_lst[i] : i for i in range(len(de_lst))}

# 아래의 경우 시간 초과 -> 컴프리헨션이 더 효율적(?)
# n_dict = {}
# for i in de_lst:
#     n_dict[i] = de_lst.index(i)

for i in lst:
    print(n_dict[i], end=' ')