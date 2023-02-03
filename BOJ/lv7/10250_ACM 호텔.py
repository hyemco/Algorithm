T = int(input())
for tc in range(T):
    h, w, n = map(int, input().split())

    if n % h == 0 and len(str(n // h)):
        ans = (h * 100) + (n // h)
    else:
        ans = ((n % h) * 100) + (n // h) + 1

    print(ans)