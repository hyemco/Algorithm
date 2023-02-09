t = int(input())
for tc in range(1, t + 1):
    s = input().strip()
    result = 0
    for i in range(len(s)//2):
        if s[i] == s[-1 - i]:
            result = 1
    print(f'#{tc} {result}')