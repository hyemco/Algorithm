t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maze = [list(input()) for _ in range(n)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    stack = []
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                stack = [(i, j)]
                break
    result = 0
    while stack:
        i, j = stack.pop()
        maze[i][j] = '1'
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] == '3':
                    result = 1
                elif maze[ni][nj] == '0':
                    stack.append((ni, nj))
    print(f'#{tc} {result}')