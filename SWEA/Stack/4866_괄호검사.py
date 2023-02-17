t = int(input())
for tc in range(1, t + 1):
    string = input()
    st = []
    ans = 0

    for s in string:
        if not st and s in ')}':
            break
        if s in '({':
            st.append(s)
        elif s == '}' and st.pop() == '(':
            break
        elif s == ')' and st.pop() == '{':
            break
    else:
        if not st:
            ans = 1
    print(f'#{tc} {ans}')