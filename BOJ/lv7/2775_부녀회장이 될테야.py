T = int(input())
for _ in range(T):
    h = int(input())
    n = int(input())
    line_0 = [i for i in range(1, n + 1)]

    for i in range(h):
        globals()[f'line_{i + 1}'] = []
        s = 0
        for j in range(n):
            s += globals()[f'line_{i}'][j]
            globals()[f'line_{i + 1}'].append(s)
    print(globals()[f'line_{i + 1}'][n - 1])