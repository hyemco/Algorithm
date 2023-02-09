t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    inp = []
    for _ in range(n):
        s, k = input().split()
        for i in range(int(k)):
            inp.append(s)

    print(f'#{tc}')
    for i in range(len(inp) // 10):
        for j in range(10):
            print(inp.pop(0), end='')
        print()
    for i in range(len(inp)):
        print(inp.pop(0), end='')
    print()
