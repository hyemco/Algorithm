def dfs(idx, lst1, lst2):
    global ans
    if idx == N:
        M = N // 2
        if len(lst1) == M:
            person1 = person2 = 0
            for i in range(M):
                for j in range(M):
                    person1 += synergy[lst1[i]][lst1[j]]
                    person2 += synergy[lst2[i]][lst2[j]]
            ans = min(ans, abs(person1 - person2))
        return
    dfs(idx + 1, lst1 + [idx], lst2)
    dfs(idx + 1, lst1, lst2 + [idx])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    ans = 20000 * N * N
    ingredient1 = []
    ingredient2 = []

    dfs(0, ingredient1, ingredient2)
    print(f'#{tc} {ans}')
