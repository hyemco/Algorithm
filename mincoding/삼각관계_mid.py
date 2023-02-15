gp_dict = {1: 'Amy ', 2: 'Edger', 3: 'Bob', 4: 'Diane', 5: 'Chloe'}
gp = [1, 2, 3, 1, 4, 3, 5, 3]
adjM = [[0] * 6 for _ in range(6)]
for i in range(4):
    v1, v2 = gp[i * 2], gp[i * 2 + 1]
    adjM[v2][v1] = 1

max_n = 0
idx = 0
i = 0
for ele in adjM:
    if ele.count(1) > max_n:
        max_n = ele.count(1)
        idx = i
    i += 1
print(gp_dict[idx])