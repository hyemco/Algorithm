def divide_group(start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    group1 = divide_group(start, mid)
    group2 = divide_group(mid + 1, end)
    return rock_paper_scissors(group1, group2)


def rock_paper_scissors(point1, point2):
    if card_lst[point1] == card_lst[point2]:
        return point1
    elif card_lst[point1] - card_lst[point2] == 1 or card_lst[point1] - card_lst[point2] == -2:
        return point1
    return point2


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    card_lst = list(map(int, input().split()))

    print(f'#{tc} {divide_group(0, n - 1) + 1}')