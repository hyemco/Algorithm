import sys
import statistics

t = int(sys.stdin.readline())
num_lst = [int(sys.stdin.readline()) for _ in range(t)]

print(round(statistics.mean(num_lst))) # 산술
print(statistics.median(num_lst))   # 중앙값
cnt_lst = sorted(statistics.multimode(num_lst))
if len(cnt_lst) > 1:
    print(cnt_lst[1])
else:
    print(*cnt_lst)

print(max(num_lst) - min(num_lst))  # 빈도