N = int(input())
M = int(input())
if M:
    broken_btn = list(map(int, input().split()))
else:
    broken_btn = []

ans = abs(N - 100)

if N == 100:
    ans = 0
elif M == 0:
    ans = min(ans, len(str(N)))
else:
    for number in range(1000000):
        for num in str(number):
            if int(num) in broken_btn:
                break
        else:
            ans = min(ans, abs(number - N) + len(str(number)))
print(ans)