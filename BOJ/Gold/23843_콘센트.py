import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
times = sorted(list(map(int, input().split())), reverse=True)
power_socket = []
for time in times:
    if len(power_socket) < M:
        heapq.heappush(power_socket, time)
    else:
        heapq.heappush(power_socket, time + heapq.heappop(power_socket))
print(max(power_socket))