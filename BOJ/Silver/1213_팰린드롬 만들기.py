words = sorted(input())
alphabet_cnt = [0] * 26
for word in words:
    alphabet_cnt[ord(word) - 65] += 1

odd = 0
odd_word = word = ''
for i in range(26):
    if alphabet_cnt[i] % 2 == 1:
        odd += 1
        odd_word += chr(i + 65)
    word += (alphabet_cnt[i] // 2) * chr(i + 65)

if odd < 2:
    print(word + odd_word + word[::-1])
else:
    print("I'm Sorry Hansoo")