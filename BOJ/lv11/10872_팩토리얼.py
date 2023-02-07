def factorial(n):
    if n == 0:
        return 1
    else:
        if n == 1:
            return n
        else:
            n = n * factorial(n - 1)
            return n


n = int(input())
print(factorial(n))