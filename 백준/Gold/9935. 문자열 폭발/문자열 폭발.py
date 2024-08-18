import sys
input = sys.stdin.readline

inp = input().rstrip()
target = input().rstrip()

stack = []
ta = len(target)

for i in range(len(inp)):
    stack.append(inp[i])
    if ''.join(stack[len(stack)-ta:]) == target:
        for _ in range(ta):
            stack.pop()

if stack: print(''.join(stack))
else : print("FRULA")