def solution(score):
    answer = []
    total = sorted([sum(i) for i in score], reverse=True)
    rank = {}
    
    tmp = (-1, 0)
    for i in total:
        if i != tmp[0]:
            rank[i] = total.index(i) + 1

    for i in score:
        answer.append(rank[sum(i)])
    return answer