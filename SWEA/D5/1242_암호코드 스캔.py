code_ratio = {
    (2, 1, 1): 0, (2, 2, 1): 1,
    (1, 2, 2): 2, (4, 1, 1): 3,
    (1, 3, 2): 4, (2, 3, 1): 5,
    (1, 1, 4): 6, (3, 1, 2): 7,
    (2, 1, 3): 8, (1, 1, 2): 9
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pw = sorted(list(set([input() for _ in range(N)])))[1:]

    ans = 0
    check = []
    for p in pw:
        binary = format(int(p, 16), 'b')

        r1 = r2 = r3 = 0
        cnt = odd_sum = even_sum = 0
        pull_code = []
        for i in range(len(binary)):
            if binary[i] == '1' and r2 == 0:
                r1 += 1
            elif binary[i] == '0' and r1 != 0 and r3 == 0:
                r2 += 1
            elif binary[i] == '1' and r2 != 0:
                r3 += 1
            elif r3 != 0:
                cnt += 1
                ratio = min(r1, r2, r3)
                code = code_ratio[(r1 // ratio, r2 // ratio, r3 // ratio)]
                pull_code.append(code)

                if cnt == 8:
                    for j in range(len(pull_code) // 2):
                        odd_sum += int(pull_code[j * 2])
                        if j != len(pull_code) // 2 - 1:
                            even_sum += int(pull_code[j * 2 + 1])
                    if (odd_sum * 3 + even_sum + pull_code[-1]) % 10 == 0 and pull_code not in check:
                        ans += odd_sum + even_sum + pull_code[-1]
                    check.append(pull_code)
                    cnt = odd_sum = even_sum = 0
                    pull_code = []
                r1 = r2 = r3 = 0

    print(f'#{tc} {ans}')