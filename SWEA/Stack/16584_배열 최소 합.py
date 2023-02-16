def backtracking(row, n, sub_sum):
    global min_sum
    if min_sum < sub_sum:
        return
    elif row == n:
        if min_sum > sub_sum:
            min_sum = sub_sum
    else:
        for i in range(n):
            # print(f'0:{i=}')
            if not visited[i]:
                # print(f'1:{i=}')
                visited[i] = True
                # print(f'1:{visited=}')
                # print(f'{row=}')
                # print(f'{sub_sum=}')
                backtracking(row + 1, n, sub_sum + num_lst[row][i])
                # print(f'2:{i=}')
                visited[i] = False
                # print(f'2:{visited=}')
                # print()


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 1000
    visited = [False] * n

    backtracking(0, n, 0)
    print(f'#{tc} {min_sum}')