t = int(input())
for i in range(t):
    s = ''
    words = input().split()
    for j in range(len(words)):
        s += words[j][::-1] + ' '

    print(s.strip())