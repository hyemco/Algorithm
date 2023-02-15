V = int(input())
adjM = [list(map(int, input().split())) for _ in range(V)]

under = []
for i in range(V):
    if adjM[i][0] == 1:
        print(f'boss:{i}')
    if adjM[0][i] == 1:
        under.append(i)
print(f'under:', end='')
print(*under)