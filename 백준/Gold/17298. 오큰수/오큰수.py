import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
lis.reverse()
stack = deque([])
result = []

for i in range(n):
    bol = False
    while stack:
        target = stack.pop()
        if lis[i] < target:
            result.append(target)
            stack.append(target)
            stack.append(lis[i])
            bol = True
            break
    if not bol:    
        stack.append(lis[i])
        result.append(-1)
result.reverse()
print(*result)