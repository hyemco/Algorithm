n, m = map(int, input().split())

for x in range(1, 3):
    globals()[f'lst_{x}'] = []
    for i in range(n):
        line = list(map(int, input().split()))
        globals()[f'lst_{x}'].append(line)

ans = lst_1
for i in range(n):
    for j in range(m):
        ans[i][j] += lst_2[i][j]

for i in ans:
    print(*i)