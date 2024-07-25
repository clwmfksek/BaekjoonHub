T = int(input())
for i in range(T):
    ps = input()
    stack = []
    for j in range(len(ps)):
        if ps[j] == '(':
            stack.append(ps[j])
        elif ps[j] == ')':
            if len(stack) == 0:
                stack.append(ps[j])
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')