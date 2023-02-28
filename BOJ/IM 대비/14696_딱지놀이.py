N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for k in range(4, 0, -1):
        if A[1:].count(k) > B[1:].count(k):
            print('A')
            break
        elif B[1:].count(k) > A[1:].count(k):
            print('B')
            break
        else:
            continue
    else:
        print('D')