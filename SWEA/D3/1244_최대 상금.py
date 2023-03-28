def dfs(cnt):
    global ans
    if cnt == count:
        tmp = int("".join(map(str, numbers)))
        ans = max(ans, tmp)
        return

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]

            is_in = int("".join(map(str, numbers)))
            if (cnt, is_in) not in visited:
                visited.append((cnt, is_in))
                dfs(cnt + 1)

            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for tc in range(1, T + 1):
    number, c = input().split()
    numbers = []
    for n in number:
        numbers.append(int(n))
    count = int(c)

    ans = 0
    visited = []
    dfs(0)
    print(f'#{tc} {ans}')