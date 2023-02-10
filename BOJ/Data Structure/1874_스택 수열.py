t = int(input())
lst = []
n = []
s = []
for _ in range(t):
    lst.append(int(input()))
start = 1
flag = 1
for i in range(t):
    while start <= lst[i]:
        n.append(start)
        s.append('+')
        start += 1

    if n[-1] == lst[i]:
        n.pop()
        s.append('-')
    else:
        print('NO')
        flag = 0
        break
if flag:
    print(*s, sep='\n')
