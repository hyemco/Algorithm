adjM = [[0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0]]

a = input()
inp = abs(ord('A') - ord(a))
ans = []
try:
    target_idx = adjM[inp].index(1)
    for i in range(8):

        if adjM[i][target_idx] == 1 and i != inp:
            i = chr(i + ord('A'))
            ans.append(i)
    if ans:
        print(*ans)
    else:
        print('없음')
except ValueError:
    print('없음')