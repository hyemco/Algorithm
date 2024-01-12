def solution(numlist, n):
    answer = []
    tmp = {}
    for i in numlist:
        tmp[i] = abs(n - i)
    tmp = sorted(tmp.items(), key=lambda x: [x[1], -x[0]])
    for i in tmp:
        answer.append(i[0])
    
    return answer