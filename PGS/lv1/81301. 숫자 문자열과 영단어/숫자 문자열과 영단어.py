def solution(s):
    num = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    answer = 0
    for i in range(10):
        if num[i] in s:
            s = s.replace(num[i], str(i))
    return int(s)