def change_to_three(num):
    tmp = ''
    while num != 0:
        tmp += str(num % 3)
        num //= 3
    return int(tmp)

def solution(n):
    answer = 0
    j = 0
    for i in str(change_to_three(n))[::-1]:
        answer += ((3 ** j) * int(i))
        j += 1
    return answer