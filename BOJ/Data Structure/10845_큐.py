import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    c = list(sys.stdin.readline().split())

    if c[0] == 'push':
        lst.append(c[1])

    elif c[0] == 'pop':
        if lst:
            print(lst[0])
            del lst[0]
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(lst))
    elif c[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        if lst:
            print(lst[0])
        else:
            print(-1)
    else:
        if lst:
            print(lst[-1])
        else:
            print(-1)