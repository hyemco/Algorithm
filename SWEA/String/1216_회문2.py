def palindrome(lst, l):
    max_l = 0
    while l <= 100:
        flag = 0
        for i in range(100):
            for j in range(101 - l):
                word = lst[i][j:j + l]
                if word == word[::-1]:
                    max_l = l
                    flag = 1
                    break
            if flag: break
        l += 1
    return max_l


for tc in range(10):
    n = int(input())
    board = [input() for _ in range(100)]

    r = palindrome(board, 1)

    turn_board = []
    for i in range(100):
        tmp = ''
        for j in range(100):
            tmp += board[j][i]
        turn_board.append(tmp)

    c = palindrome(turn_board, 1)
    print(f'#{n} {max(r, c)}')