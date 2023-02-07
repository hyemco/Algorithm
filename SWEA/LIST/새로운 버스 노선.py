T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    stations = [0 for _ in range(1001)]
    for _ in range(N):
        a, b, c = map(int, input().split())
        if a == 1:
            for i in range(b, c + 1):
                stations[i] += 1
        elif a == 2:
            for i in range(b, c + 1, 2):
                stations[i] += 1
        elif a == 3:
            if b % 2 == 1:
                for i in range(b, c + 1):
                    if i % 3 == 0 and i % 10 != 0:
                        stations[i] += 1
            else:
                for i in range(b, c + 1):
                    if i % 4 == 0:
                        stations[i] += 1
    print(f'#{test_case} {max(stations)}')