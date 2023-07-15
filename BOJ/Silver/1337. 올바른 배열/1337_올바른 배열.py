N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()
temp = []

for i in range(N):
    cnt = 0
    for num in range(numbers[i], numbers[i] + 5):
        if num not in numbers:
            cnt += 1
    temp.append(cnt)
    if cnt == 0:
        break

print(min(temp))