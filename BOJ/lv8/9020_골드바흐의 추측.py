def prime_number(a):
    for j in range(2, int(a**0.5) + 1):
        if a % j == 0:
            return 1
    return 0


t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    for i in range(n // 2, n + 1):
        if prime_number(i) == 0 and prime_number((n - i)) == 0:
            ans.append(i)
            ans.append(n - i)
            break
    print(*sorted(ans))