s = list(input())
stack = []
ans = ''
for i in s:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            stack.append(i)
        elif i in '*/':
            while stack and stack[-1] in '*/':
                ans += stack.pop()
            stack.append(i)
        elif i in '+-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
while stack:
    ans += stack.pop()

print(ans)