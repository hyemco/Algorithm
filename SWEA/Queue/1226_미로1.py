from collections import deque

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    maze[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for d in delta:
            ny, nx = y + d[0], x + d[1]
            if 1 <= ny < 14 and 1 <= nx < 14:
                if maze[ny][nx] == 3:
                    return 1
                elif maze[ny][nx] == 0:
                    maze[ny][nx] = 1
                    queue.append((ny, nx))
    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    print(f'#{tc} {bfs(1, 1)}')