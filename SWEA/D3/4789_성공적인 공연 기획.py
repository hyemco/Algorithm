T = int(input())
for tc in range(1, T + 1):
    clap = list(map(int, input()))

    ans = people = 0
    for i in range(len(clap)):
        if clap[i]:
            if people < i:
                ans += (i - people)
                people += (i - people)
        people += clap[i]
    print(f'#{tc} {ans}')