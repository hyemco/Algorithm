R, C = map(int, input().split())
hall = [[0] * C for _ in range(R)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = 1
i, j = 0, -1
while n < R * C:
    for d in delta:
        i, j = i + d[0], j + d[1]
        while 0 <= i < R and 0 <= j < C and hall[i][j] == 0:
            hall[i][j] = n
            n += 1
            i, j = i + d[0], j + d[1]
        i, j = i - d[0], j - d[1]

target = int(input())

if target > R * C:
    print(0)
else:
    for i in range(R):
        for j in range(C):
            if hall[i][j] == target:
                print(i + 1, j + 1)
                break
        else:
            continue
        break