N, K = map(int, input().split())
w = [0] * 7
m = [0] * 7

ans = 0
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        w[Y] += 1
    elif S == 1:
        m[Y] += 1
for i in range(1, 7):
    if w[i] % K == 0:
        ans += w[i] // K
    elif w[i] % K != 0:
        ans += w[i] // K + 1
    if m[i] % K == 0:
        ans += m[i] // K
    elif m[i] % K != 0:
        ans += m[i] // K + 1

print(ans)