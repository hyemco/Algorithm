N = int(input())
d = [0] * (N + 1)
'''
d[i] : i(인덱스 번호)가 1이 되는데 필요한 연산 횟수
d[1] = 1, d[2] = 2, d[3] = 1
'''

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1     # 1을 빼는 경우
    if i % 3 == 0:          # 3으로 나눠질 경우
        d[i] = min(d[i // 3] + 1, d[i])
    if i % 2 == 0:          # 2로 나눠질 경우
        d[i] = min(d[i // 2] + 1, d[i])

ans = d[N]
print(ans)