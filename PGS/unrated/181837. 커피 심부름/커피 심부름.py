def solution(order):
    tmp = [i for i in order if 'latte' in i]
    lenL = len(tmp)
    return lenL * 5000 + ((len(order) - lenL) * 4500)