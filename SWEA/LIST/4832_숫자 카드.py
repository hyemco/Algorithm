from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = input()
    number_lst = []

    # Counter 함수 사용 x
    for i in numbers:
        number_lst.append(int(i))
    number_lst.sort()
    cnt_lst = [0 for _ in range(max(number_lst) + 1)]

    for j in number_lst:
        cnt_lst[j] += 1

    idx_lst = list(filter(lambda x: cnt_lst[x] == max(cnt_lst), range(len(cnt_lst))))

    print(f'#{test_case} {max(idx_lst)} {max(cnt_lst)}')

    ## Counter 함수 사용
    # c = Counter(numbers)
    # order = c.most_common()
    # max_num = order[0][1]
    #
    # repeat_num = []
    # for num in order:
    #     if num[1] == max_num:
    #         repeat_num.append(num[0])
    # print(f'#{test_case} {max(repeat_num)} {max_num}')