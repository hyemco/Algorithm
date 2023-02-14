V, E = map(int, input().split())
adjM = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e = map(int, input().split())
    adjM[s - 1][e - 1] = 1

for ele in adjM:
    print(*ele)