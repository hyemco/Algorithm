def binary(n):
    global cnt
    global s
    if n == 0:
        return s
    elif cnt > 12:
        return 'overflow'
    else:
        cnt += 1
        s += str(int(n * 2))
        return binary(n * 2 - int(n * 2))


T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    cnt = 0
    s = ''
    print(f'#{tc} {binary(N)}')