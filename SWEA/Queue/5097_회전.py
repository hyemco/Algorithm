t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(m):
        lst.append(lst.pop(0))
    print(f'#{tc} {lst[0]}')