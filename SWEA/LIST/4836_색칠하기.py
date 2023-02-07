T = int(input())
for test_case in range(1, T + 1):
    box = [[0] * 10 for _ in range(10)]
    n = int(input())
    for _ in range(n):
        inp = list(map(int, input().split()))
        for i in range(inp[1] - 1, inp[3]):
            for j in range(inp[0] - 1, inp[2]):
                box[i][j] += inp[4]
        cnt = 0
        for i in box:
            for j in i:
                if j > 2:
                    cnt += 1
    print(f'#{test_case} {cnt}')