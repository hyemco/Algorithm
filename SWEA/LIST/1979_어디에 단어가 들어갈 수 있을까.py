t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 0:
                if cnt == k:
                    ans += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == k:
            ans += 1

    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[j][i] == 0:
                if cnt == k:
                    ans += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == k:
            ans += 1
    print(f'#{tc} {ans}')