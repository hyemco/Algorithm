t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cnt = [0] * 201
    for i in range(n):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        s = (s + 1) // 2
        e = (e + 1) // 2
        for j in range(s, e + 1):
            cnt[j] += 1
    print(f'#{tc} {max(cnt)}')