t = int(input())
for tc in range(1, t + 1):
    s = input()
    lst = []
    ans = 1
    for i in s:
        if i == '(' or i == '{':
            lst.append(i)
        elif i == ')' or i == '}':
            if len(lst) == 0:
                ans = 0
                break
            elif i == ')' and lst.pop() == '{':
                ans = 0
                break
            elif i == '}' and lst.pop() == '(':
                ans = 0
                break
    if len(lst):
        ans = 0
    print(f'#{tc} {ans}')