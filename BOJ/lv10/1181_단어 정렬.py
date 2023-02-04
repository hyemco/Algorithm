import sys
input = sys.stdin.readline
t = int(input())
letters = {}
for _ in range(t):
    a = input().strip()
    letters[a] = len(a)

letters = sorted(letters.items(), key=lambda x: (x[1], x[0]))
for i in letters:
    print(i[0])