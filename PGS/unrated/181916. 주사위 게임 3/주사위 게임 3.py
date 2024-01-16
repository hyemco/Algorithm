def solution(a, b, c, d):
    answer = 0
    tmp = [a, b, c, d]
    cnt = {}
    for i in tmp:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    cnt = sorted(cnt.items(), key= lambda x:(x[1], x[0]), reverse=True)
    
    if len(cnt) == 1:
        return cnt[0][0] * 1111
    elif len(cnt) == 2:
        if cnt[0][1] == 3:
            return (cnt[0][0] * 10 + cnt[1][0]) ** 2
        else:
            return (cnt[0][0] + cnt[1][0]) * abs(cnt[0][0] - cnt[1][0])
    elif len(cnt) == 3:
        return cnt[1][0] * cnt[2][0]
    else:
        return cnt[-1][0]