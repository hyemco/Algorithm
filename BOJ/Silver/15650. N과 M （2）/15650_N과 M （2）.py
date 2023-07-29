def dfs(start):
    if len(numbers) == M:
        print(' '.join(map(str, numbers)))
        return

    for i in range(start, N + 1):
        if i not in numbers:
            numbers.append(i)
            dfs(i + 1)
            numbers.pop()


N, M = map(int, input().split())
numbers = []
dfs(1)