t = int(input())
for tc in range(1, t + 1):
    text = input()
    lst = []
    for char in text:
        if lst:
            if lst[-1] != char:
                lst.append(char)
            else:
                del lst[-1]
        else:
            lst.append(char)
    print(f'#{tc} {len(lst)}')