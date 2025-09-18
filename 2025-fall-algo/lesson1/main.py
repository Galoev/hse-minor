# (()()) -> YES
# )( -> NO
# ()) -> NO

s = "()()(((((()"
stack = []
wrong = False
for ch in s:
    if ch == '(':
        stack.append(ch)
    elif len(stack) > 0:
        stack.pop()
    else:
        wrong = True
        break

if wrong or len(stack) > 0:
    print('NO')
else:
    print('YES')
