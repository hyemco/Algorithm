N = int(input())
numbers = list(map(int, input().split()))
inc_cnt = dec_cnt = 1
ans = 1

for i in range(N - 1):
    if numbers[i] <= numbers[i + 1]:
        inc_cnt += 1
    else:
        inc_cnt = 1
    if ans < inc_cnt:
        ans = inc_cnt

for i in range(N - 1):
    if numbers[i] >= numbers[i + 1]:
        dec_cnt += 1
    else:
        dec_cnt = 1
    if ans < dec_cnt:
        ans = dec_cnt
print(ans)