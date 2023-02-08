t = int(input())
for tc in range(1, t + 1):
    t, n = input().split()
    num_lst = list(input().split())

    str_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    idx_lst = []
    for i in range(int(n)):
        idx_lst.append(str_lst.index(num_lst[i]))

    idx_lst.sort()

    for i in range(int(n)):
        idx_lst[i] = str_lst[idx_lst[i]]
    print(t)
    print(*idx_lst)