def solution(n):
    answer = []
        
    for i in range(1, n + 1):
        if i in answer:
            break
        else:
            if n % i == 0:
                answer.append(i)
                answer.append(n // i)
    return sorted(set(answer))