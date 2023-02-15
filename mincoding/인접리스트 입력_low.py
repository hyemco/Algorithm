V, E = map(int, input().split())
adjL = [[] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    s, e = map(int, input().split())
    adjL[s].append(e)

i = 0
for ele in adjL:
    if ele:
        print(f'{i} :', *ele)
    i += 1