import sys

N, K = map(int, sys.stdin.readline().split())
temperature = list(map(int, sys.stdin.readline().split()))

rlt = [sum(temperature[:K])]

for i in range(N - K):
    rlt.append(rlt[i] - temperature[i] + temperature[K + i])

print(max(rlt))