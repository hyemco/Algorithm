def divide(n, mul, mod):
    if mul == 1:
        return n % mod
    elif mul % 2 == 0:
        return (divide(n, mul // 2, mod) ** 2) % mod
    else:
        return ((divide(n, mul // 2, mod) ** 2) * n) % mod


A, B, C = map(int, input().split())
print(divide(A, B, C))