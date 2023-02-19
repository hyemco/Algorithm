move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    global queue
    count = 0
    while queue:
        temp = []
        while queue:
            y, x = queue.pop()
            for i, j in move:
                dy = y + i
                dx = x + j
                if 0 <= dy < N and 0 <= dx < N:
                    if not map_list[dy][dx]:
                        map_list[dy][dx] = 1
                        temp.append((dy, dx))
                    if map_list[dy][dx] == 3:
                        return count
        count += 1
        queue = temp


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    queue = []
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == 2:
                queue.append((i, j))
                break
        else:
            continue
        break
    print(f'#{tc} {bfs()}')
