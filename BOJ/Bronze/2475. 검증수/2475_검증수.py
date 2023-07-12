numbers = list(map(int, input().split()))

square_number = 0
for number in numbers:
    square_number += number * number

print(square_number % 10)