T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)

    ans = idx = 0
    for w in weight:
        if truck[idx] >= w:
            ans += w
            idx += 1
            if idx == M:
                break
    print(f'#{tc} {ans}')