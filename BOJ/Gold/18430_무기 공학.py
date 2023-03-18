def back_tracking(i, j, total):
    global ans
    if j == M:
        i += 1
        j = 0
    if i == N:
        ans = max(ans, total)
        return
    if not visited[i][j]:
        for k in range(4):
            x1, y1, x2, y2 = boomerang[k]
            n_x1, n_y1, n_x2, n_y2 = i + x1, j + y1, i + x2, j + y2
            if 0 <= n_x1 < N and 0 <= n_y1 < M and 0 <= n_x2 < N and 0 <= n_y2 < M:
                if not visited[n_x1][n_y1] and not visited[n_x2][n_y2]:
                    visited[i][j] = visited[n_x1][n_y1] = visited[n_x2][n_y2] = True
                    tmp_total = total + strength[i][j] * 2 + strength[n_x1][n_y1] + strength[n_x2][n_y2]
                    back_tracking(i, j + 1, tmp_total)
                    visited[i][j] = visited[n_x1][n_y1] = visited[n_x2][n_y2] = False
    back_tracking(i, j + 1, total)


N, M = map(int, input().split())
strength = [list(map(int, input().split())) for _ in range(N)]
boomerang = {
    0: [0, -1, 1, 0],
    1: [-1, 0, 0, -1],
    2: [-1, 0, 0, 1],
    3: [0, 1, 1, 0]
}
visited = [[False] * M for _ in range(N)]
ans = 0
back_tracking(0, 0, 0)
print(ans)