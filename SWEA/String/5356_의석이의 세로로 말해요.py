t = int(input())
for tc in range(1, t + 1):
    max_l = 0
    lst = []
    for i in range(5):
        nums = list(input())
        lst.append(nums)
        if len(nums) > max_l:
            max_l = len(nums)

    print(f'#{tc}', end=' ')
    for i in range(max_l):
        for j in range(5):
            try:
                print(lst[j][i], end='')
            except IndexError:
                pass
    print()