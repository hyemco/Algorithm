import sys

n = int(sys.stdin.readline())
cnt = 0

if len(str(n)) == 1:
    n = '0' + str(n)
else:
    n = str(n)

temp1 = n
while True:
    temp2 = int(temp1[0]) + int(temp1[1])

    if len(str(temp2)) == 1:
        temp2 = '0' + str(temp2)
    else:
        temp2 = str(temp2)

    temp1 = str(temp1[1] + temp2[1])
    cnt += 1

    target = int(temp1)
    if temp1 == n:
        break
print(cnt)