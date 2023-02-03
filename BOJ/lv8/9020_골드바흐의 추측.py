def prime_number(n):
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return 1
    return 0


t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    for i in range(n // 2, n + 1):
        if prime_number(i) == 0 and prime_number((n - i)) == 0:

            break



    # n 까지의 소수 넣기
    # prime_num = []
    # for i in range(2, n + 1):
    #     if prime_number(i) == 0:
    #         prime_num.append(i)
    # # 짝 찾기
    # temp = []
    # for num in prime_num:
    #     mid = int(len(prime_num) / 2)
    #     while True:
    #         if (n - prime_num[mid]) in prime_num:
    #             temp.append(n - prime_num[mid])
    #             temp.append(prime_num[mid])
    #             break
    #         else:
    #             mid -= 1
    # temp = sorted(list(set(temp)))
    # if len(temp) == 1:
    #     print(temp[0], temp[0])
    # else:
    #     print(temp[0], temp[1])