def is_run(lst):
    for i in range(8):
        if lst[i] and lst[i + 1] and lst[i + 2]:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]
    ans = 0
    for i in range(0, 12, 2):
        player1[cards[i]] += 1
        player2[cards[i + 1]] += 1

        if i > 3:
            if is_run(player1) or player1[cards[i]] == 3:
                ans = 1
                break
            if is_run(player2) or player2[cards[i + 1]] == 3:
                ans = 2
                break
    print(f'#{tc} {ans}')
