n1, n2 = map(int, input().split())

ans = []
for i in range(n1, n2 + 1):
    flag = True
    if i > 1:
        for j in range(2, round(i**0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            ans.append(i)

print(*ans, sep='\n')