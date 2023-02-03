n = int(input())

ans = []
if n != 1:
    while n > 1:
        for i in range(2, n + 2):
            if n % i == 0:
                n //= i
                ans.append(i)
                break

if len(ans) != 0:
    for _ in sorted(ans):
        print(_)
else:
    print()