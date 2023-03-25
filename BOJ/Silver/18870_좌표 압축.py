import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
set_numbers = sorted((list(set(numbers))))
order = {}
for i in range(len(set_numbers)):
    order[set_numbers[i]] = i

for number in numbers:
    print(order[number], end=' ')