import sys

target = list(sys.stdin.readline().rstrip())
tmp = []

for i in range(int(sys.stdin.readline())):
    c = list(sys.stdin.readline().split())
    if c[0] == 'L':
        if target:
            tmp.append(target.pop())
    elif c[0] == 'D':
        if tmp:
            target.append(tmp.pop())
    elif c[0] == 'B':
        if target:
            target.pop()
    elif c[0] == 'P':
        target.append(c[1])

target.extend(reversed(tmp))
print(*target, sep='')