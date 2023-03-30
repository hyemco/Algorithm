def make_ternary(n):
    str_ternary = []
    while n >= 1:
        n, mod = divmod(n, 3)
        str_ternary.append(mod)
    return str_ternary


def func():
    for i in range(len(binary)):
        binary[i] = (binary[i] + 1) % 2

        # 2진수 -> 10진수
        num = 0
        for b in binary:
            num = num * 2 + b

        # 10진수 -> 3진수
        ch_ternary = make_ternary(num)

        cnt = 0
        rev_ternary = ternary[::-1]
        for j in range(min(len(ch_ternary), len(rev_ternary))):
            if ch_ternary[j] != rev_ternary[j]:
                cnt += 1
        cnt += abs(len(ch_ternary) - len(rev_ternary))
        if cnt == 1:
            return num
        binary[i] = (binary[i] + 1) % 2


T = int(input())
for tc in range(1, T + 1):
    binary = list(map(int, input()))
    ternary = list(map(int, input()))

    ans = func()
    print(f'#{tc} {ans}')