from sys import stdin
from collections import deque


def bfs(arr):
    cases = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


    visited = [False] * 512       # 동전 배치 경우의 수 : 9자리 2^9
    visited[int(''.join(arr), 2)] = True

    Q = deque([(int(''.join(arr), 2), 0)])
    while Q:
        idx, count = Q.popleft()

        if idx == 0 or idx == 511:
            return count

        for nums in cases:
            newArr = change(nums, list(bin(idx)[2:].zfill(9)))
            vs = int(''.join(newArr), 2)
            if not visited[vs]:
                visited[vs] = True
                Q.append((int(''.join(newArr), 2), count + 1))

    return -1


def change(nums, arr):
    for num in nums:
        if arr[num] == '1':
            arr[num] = '0'
        else:
            arr[num] = '1'
    return arr


T = int(stdin.readline())

for _ in range(T):
    graph = list(list(stdin.readline().split()) for _ in range(3))
    graph = ['1' if graph[i][j] == 'H' else '0' for i in range(3) for j in range(3)]
    print(bfs(graph))