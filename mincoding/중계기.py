import math

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    village = [list(map(int, input().split())) for _ in range(N + 1)]

    house = []
    for i in range(N + 1):
        for j in range(N + 1):
            if village[i][j] == 2:
                repeater = i, j
            if village[i][j] == 1:
                house.append((i, j))
    max_distance = 0
    for i, j in house:
        distance = (i - repeater[0]) ** 2 + (j - repeater[1]) ** 2
        if max_distance < distance:
            max_distance = distance

    # 방법1) math.ceil 사용
    # ans = math.ceil(max_distance ** (1 / 2))

    # 방법2) 정수로 떨어지는지 아닌지를 보고 값 구분
    if (max_distance ** (1 / 2)) % 1 > 0.0:
        ans = int(max_distance ** (1 / 2)) + 1
    else:
        ans = int(max_distance ** (1 / 2))

    print(f'#{tc} {ans}')