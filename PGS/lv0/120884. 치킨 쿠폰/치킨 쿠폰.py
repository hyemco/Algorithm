def solution(chicken):
    answer = chicken // 10
    now = answer
    c = chicken % 10
    while now // 10 > 0:
        answer += now // 10
        c += now % 10
        if c > 9:
            answer += 1
            c = now % 10
        now //= 10
    c += now
    if c > 9:
        answer += 1
    return answer