def solution(s):
    answer = 0
    s = s.split(' ')[::-1]
    i = 0
    while i < len(s):
        if s[i] == 'Z':
            i += 2
        else:
            answer += int(s[i])
            i += 1
            
    return answer