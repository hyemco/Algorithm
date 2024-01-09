def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split()
        tmp = int(q[0])
        for i in range(len(q)):
            if q[i] == '+':
                tmp += int(q[i + 1])
            elif q[i] == '-':
                tmp -= int(q[i + 1])
            elif q[i] == '=':
                if tmp == int(q[i+ 1]):
                    answer.append('O')
                else:
                    answer.append('X')
            else:
                continue
    return answer