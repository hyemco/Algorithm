def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            t = ord(i) + n
            if i.isupper():
                if t > 90:
                    answer += chr(t - 26)
                else:
                    answer += chr(t)
            else:
                if t > 122:
                    answer += chr(t - 26)
                else:
                    answer += chr(t)
        else:
            answer += i
    return answer