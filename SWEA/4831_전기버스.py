T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_stations = list(map(int, input().split()))
    current_loca = 0
    cnt = 0

    while current_loca + K < N:
        for jump in range(K, 0, -1): # 이 범위 안에 충전기 있다면 거기로 이동
            if (current_loca + jump) in charge_stations:
                current_loca += jump
                cnt += 1
                break
        else:
            cnt = 0
            break
    print('#{} {}'.format(test_case, cnt))