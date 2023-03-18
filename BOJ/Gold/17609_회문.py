import sys
input = sys.stdin.readline


def is_palindrome(word):
    start = 0
    end = len(word) - 1

    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1

        else:
            if start + 1 <= end:
                tmp = word[:start] + word[start + 1:]
                if tmp == tmp[::-1]:
                    return 1
            if start <= end - 1:
                tmp = word[:end] + word[end + 1:]
                if tmp == tmp[::-1]:
                    return 1
            return 2
    return 0


T = int(input())
for _ in range(T):
    target = input().strip()
    print(is_palindrome(target))