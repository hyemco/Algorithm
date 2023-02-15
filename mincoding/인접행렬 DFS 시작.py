V = int(input())
adjM = [list(map(int, input().split())) for _ in range(V)]
stack = [0]
ans = ''
while stack:
    target = stack.pop()
    ans += str(target) + ' '
    for i in range(V - 1, -1, -1):
        if adjM[target][i] == 1:
            stack.append(i)
print(ans)