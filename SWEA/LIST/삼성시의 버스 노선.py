T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt = {}

    for i in range(1, 5001):
        cnt[i] = 0

    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            cnt[i] += 1

    P = int(input())
    ans = []
    for _ in range(P):
        idx = int(input())
        ans.append(cnt[idx])
    print(f'#{test_case}', *ans)