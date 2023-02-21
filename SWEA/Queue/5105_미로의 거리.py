from collections import deque

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(graph):
    global queue
    cnt = 0
    while queue:
        temp = deque()
        while queue:
            y, x = queue.popleft()
            for i, j in delta:
                dy, dx = i + y, j + x
                if 0 <= dy < N and 0 <= dx < N:
                    if graph[dy][dx] == 2:
                        return cnt
                    elif not graph[dy][dx]:
                        graph[dy][dx] = 1
                        temp.append((dy, dx))
        cnt += 1
        queue = temp


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                queue.append((i, j))
                ans = bfs(maze)
                break
        else:
            continue
        break
    if not ans:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc} {ans}')
