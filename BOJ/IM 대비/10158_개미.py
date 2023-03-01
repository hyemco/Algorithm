w, h = map(int, input().split())
i, j = map(int, input().split())
target = int(input())

n1 = (i + target) // w
n2 = (j + target) // h

if n1 % 2 == 0:
    x = (i + target) % w
else:
    x = w - (i + target) % w

if n2 % 2 == 0:
    y = (j + target) % h
else:
    y = h - (j + target) % h

print(x, y)