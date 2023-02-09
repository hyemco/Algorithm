t = int(input())
for tc in range(1, t + 1):
    p, s = input(), input()
    m, n = len(p), len(s)

    cnt = [0] * m

    for i in range(n):
        for j in range(m):
            if p[j] == s[i]:
                cnt[j] += 1

    print(f'#{tc} {max(cnt)}')