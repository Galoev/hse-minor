print(sum(list(map(int, open('input.txt').readlines()))))
# () () { [] { [()] }}


s = "()()(((((()"
stack = []
wrong = False
for ch in s:
    if ch == '(' or ch == '{':
        stack.append(ch)
    else:
        if len(stack) == 0:
            wrong = True
            break
        stack.pop()

if wrong or len(stack) > 0:
    print('NO')
else:
    print('YES')