N = int(input())
switch = [0] + list(map(int, input().split()))
s_N = int(input())
for _ in range(s_N):
    sex, t = map(int, input().split())

    if sex == 1:
        for i in range(t, N + 1, t):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1

    elif sex == 2:
        k = 1
        while True:
            if 0 < t - k <= N and 0 < t + k <= N and switch[t - k] == switch[t + k]:
                k += 1
            else:
                for i in range(t - (k - 1), t + k):
                    if switch[i] == 1:
                        switch[i] = 0
                    else:
                        switch[i] = 1
                break

for i in range(1, N + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()