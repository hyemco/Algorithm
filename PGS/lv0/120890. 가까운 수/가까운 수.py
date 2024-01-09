def solution(array, n):
    answer = 0
    array.sort()
    tmp = 100 + n
    
    for i in array:
        if tmp > abs(n - i):
            tmp = abs(n - i)
            answer = i

    return answer