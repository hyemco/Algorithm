R, C = map(int, input().split())
maps = []
for _ in range(R):
    maps.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sink = []
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'X':   # 땅인 경우 세면 이상 바다인지 확인
            count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    if maps[nx][ny] == '.':
                        count += 1  # 바다인 경우 cnt 값 증가
                else:
                    count += 1      # 범위 벗어나도 cnt 값 증가
                    continue
            if count >= 3:
                sink.append((i, j))

# 바다로 바꾸기
if len(sink) > 0:
    for x, y in sink:
        maps[x][y] = '.'

x1 = 0
y1 = C - 1
x2 = 0
y2 = 0
for i in range(0, R):
    if 'X' in maps[i]:
        x1 = i
        break
for i in range(R - 1, -1, -1):
    if 'X' in maps[i]:
        x2 = i
        break

for i in range(x1, x2 + 1):
    for j in range(C):
        if maps[i][j] == 'X':
            y1 = min(y1, j)
            y2 = max(y2, j)

for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        print(maps[i][j], end='')
    print()