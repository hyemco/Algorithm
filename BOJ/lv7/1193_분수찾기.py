X = int(input())

temp = 0
line = 0
while temp < X:
    line += 1
    temp += line

a = line - (temp - X)
if line == 1:
    print('1/1')
elif line % 2:
    print(f'{line - a + 1}/{a}')
else:
    print(f'{a}/{line - a + 1}')