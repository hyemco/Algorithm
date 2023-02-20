def f():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    for i in range(1, n + 1):
        if i in lst:
            continue
        lst.append(i)
        f()
        lst.pop()


n, m = map(int, input().split())
lst = []
f()