T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    Q = []
    max_cnt = 0
    # room = []
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for x in range(N):
        for y in range(N):
            cnt = 1
            Q = [(x, y)]
            while Q:
                i, j = Q.pop()
                for d in delta:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < N and 0 <= nj < N:
                        if rooms[ni][nj] == rooms[i][j] + 1:
                            cnt += 1
                            Q.append((ni, nj))
                            break
            if max_cnt < cnt:
                max_cnt = cnt
                room = (rooms[x][y])
            elif max_cnt == cnt:
                room = min(room, rooms[x][y])
    print(f'#{tc} {room} {max_cnt}')