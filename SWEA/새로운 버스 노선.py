T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    station_lst = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        if len(station_lst) - 1 < c:
            station_lst += [0] * (c - len(station_lst) + 1)
        if a == 1:
            for i in range(b, c + 1):
                station_lst[i] += 1
        elif a == 2:
            station_lst[b] += 1
            station_lst[c] += 1
            if b % 2:
                for i in range(b + 1, c):
                    if i % 2:
                        station_lst[i] += 1
            else:
                for i in range(b + 1, c):
                    if i % 2 == 1:
                        station_lst[i] += 1
        else:
            station_lst[b] += 1
            station_lst[c] += 1
            if b % 2:
                for i in range(a + 1, b):
                    if i % 3 == 0 and i % 10 == 1:
                        station_lst[i] += 1
            else:
                for i in range(b + 1, c):
                    if i % 4 == 0:
                        station_lst[i] += 1
    print(f'#{test_case} {max(station_lst)}')