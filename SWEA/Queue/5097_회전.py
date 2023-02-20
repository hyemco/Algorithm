T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    front = 0
    front += M % N
    print(f'#{tc} {num_lst[front]}')