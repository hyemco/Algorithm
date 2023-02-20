T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = int((N - 1) ** (1 / 3)) + 1
    if X ** 3 == N:
        print(f'#{tc} {X}')
    else:
        print(f'#{tc}', -1)