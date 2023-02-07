for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    ans = 0
    for i in range(2, N - 2):
        # 좌우 2개씩 총 4개에 대한 차 구하기
        before1 = buildings[i] - buildings[i-2]
        before2 = buildings[i] - buildings[i-1]
        after1 = buildings[i] - buildings[i+1]
        after2 = buildings[i] - buildings[i+2]
        if before1 > 0 and before2 > 0 and after1 > 0 and after2 > 0:
            ans += min(before1, before2, after1, after2)

    print(f'#{test_case} {ans}')