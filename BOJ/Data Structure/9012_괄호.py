t = int(input())
for _ in range(t):
    s = input()
    cnt = 0
    ans = 'YES'
    for i in range(len(s)):
        if cnt == 0:
            if s[i] != '(':
                ans = 'NO'
                break
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt -= 1
    if cnt != 0:
        ans = 'NO'
    print(ans)