n1 = int(input())
n2 = int(input())

prime_number_lst = []
for i in range(n1, n2 + 1):
    flag = True
    if i > 1:
        for j in range(2, round((i**0.5)) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            prime_number_lst.append(i)

if len(prime_number_lst) == 0:
    print(-1)
else:
    print(sum(prime_number_lst))
    print(min(prime_number_lst))






