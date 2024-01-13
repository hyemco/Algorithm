def solution(dots):
    answer = 0
    dots = sorted(dots, key=lambda x:x[0])
    a, b, c, d = 0, 0, 0, 0
    tmp = []
    for i in range(2):
        if len(tmp) < 1:
            a = (dots[i][0] - dots[i + 1][0], dots[i][1] - dots[i + 1][1])
            b = (dots[i][0] - dots[i + 2][0], dots[i][1] - dots[i + 2][1])
            tmp.append(a)
            tmp.append(b)
        else:
            c = (dots[i + 1][0] - dots[i + 2][0], dots[i+ 1][1] - dots[i + 2][1])
            d = (dots[i][0] - dots[i + 2][0],dots[i][1] - dots[i + 2][1])
            tmp.append(c)
            tmp.append(d)
    print(dots)
    print(a, b, c, d)
    if a == c or b == d:
        return 1
    for i in tmp:
        if i[0] == i[1]:
            return 1
    
    return 0