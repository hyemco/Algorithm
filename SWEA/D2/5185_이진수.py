def binary(n):
    if n < 2:
        return str(n)
    else:
        return binary(n // 2) + binary(n % 2)


T = int(input())
for tc in range(1, T + 1):
    N, num = input().split()
    ans = ''
    for i in num:
        if i.isdigit():
            tmp = binary(int(i))
        elif i.isalpha():
            tmp = binary(ord(i) - 55)
        ans += '0' * (4 - len(tmp)) + tmp
    print(f'#{tc} {ans}')