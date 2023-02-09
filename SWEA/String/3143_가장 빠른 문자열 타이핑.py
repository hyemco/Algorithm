t = int(input())
for tc in range(1, t + 1):
    s, p = input().split()
    n, m = len(s), len(p)
    ans = 0
    i = 0

    while i <= n - m:
        c = ''
        for j in range(i, i + m):
            c += s[j]
        if c != p:
            ans += 1
            i += 1
        else:
            ans += 1
            i += m
    ans += n - i
    print(f'#{tc} {ans}')
