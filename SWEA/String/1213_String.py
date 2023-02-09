for _ in range(10):
    tc = int(input())
    p, s = input(), input()
    m, n = len(p), len(s)
    ans = 0

    for i in range(n - m + 1):
        cnt = 0
        for j in range(m):
            if s[i + j] != p[j]:
                break
            else:
                cnt += 1
            if cnt == m:
                cnt = 0
                ans += 1

    print(f'#{tc} {ans}')