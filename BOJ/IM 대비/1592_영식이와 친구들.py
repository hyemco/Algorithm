N, M, L = map(int, input().split())
person = [1] + [0] * (N - 1)
ans = i = 0
while M not in person:
    if person[i] % 2:
        person[(i + L) % N] += 1
        i = (i + L) % N
    else:
        person[(N + (i - L)) % N] += 1
        i = (N + (i - L)) % N
    ans += 1
print(ans)