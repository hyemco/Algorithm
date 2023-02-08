t = int(input())
for tc in range(1, t + 1):
    p = input()
    s = input()
    p_l = len(p)
    s_l = len(s)
    i = p_l - 1
    flag = 0

    while i < s_l:
        if s[i] == p[-1]:
            for j in range(p_l):
                if s[i - j] != p[-1 - j]:
                    i += 1
                    break
            else:
                flag = 1
                i = s_l
        else:
            for j in range(1, p_l):
                if s[i] == p[-1 - j]:
                    i += j
                    break
            else:
                i += p_l
    print(f'#{tc} {flag}')