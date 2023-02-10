import sys

def push(lst, a):
    lst.append(a)
    return lst

def pop(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[len(lst) - 1])
        del lst[len(lst) - 1]

def size(lst):
    print(len(lst))

def empty(lst):
    if len(lst) == 0:
        print(1)
    else:
        print(0)

def top(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[len(lst) - 1])

lst = []
n = int(sys.stdin.readline())
for i in range(n):
    a = sys.stdin.readline().split()
    if len(a) == 2:
        o = a[0]
        t = int(a[1])
    else:
        o = a[0]
    if o == 'push':
        push(lst, t)
    elif o == 'pop':
        pop(lst)
    elif o == 'size':
        size(lst)
    elif o == 'empty':
        empty(lst)
    elif o == 'top':
        top(lst)