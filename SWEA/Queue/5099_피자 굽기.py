from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = deque(enumerate(list(map(int, input().split())), 1))
    oven = deque()
    for _ in range(N):
        oven.append(cheeses.popleft())

    while len(oven) > 1:
        if len(oven) < N and cheeses:
            oven.append(cheeses.popleft())
        idx, cheese = oven.popleft()
        if not cheese // 2:
            continue
        else:
            oven.append((idx, cheese // 2))
    print(f'#{tc} {oven.popleft()[0]}')