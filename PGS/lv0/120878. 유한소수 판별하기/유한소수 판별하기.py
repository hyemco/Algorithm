def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(a, b):
    answer = 0
    if a == b:
        return 1
    b //= gcd(a, b)
    while b != 1:
        if b % 2 != 0 and b % 5 != 0:
            return 2
        else:
            if b % 2 == 0:
                b //= 2
            else:
                b //= 5
    return 1