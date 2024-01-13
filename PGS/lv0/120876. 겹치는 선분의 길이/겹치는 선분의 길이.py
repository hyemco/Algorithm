def solution(lines):
    answer = 0
    lines = sorted(lines, key= lambda x: x[0])
    line = {}
    
    for a, b, in lines:
        while a < b:
            if (a, a + 1) not in line:
                line[(a, a + 1)] = 1
            else:
                line[(a, a + 1)] += 1
            a += 1
    for i in line.values():
        if i > 1:
            answer += 1
    return answer