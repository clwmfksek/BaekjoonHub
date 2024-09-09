import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = deque([deque([]) for i in range(n)])

indgree = [0 for i in range(n)]

for i in range(m):
    num1,num2 = map(int,input().split())
    num1 -= 1
    num2 -= 1
    graph[num1].append(num2)
    indgree[num2] += 1
queue = deque([])

for i in range(len(graph)):
    if not indgree[i]:
        queue.append(i)

result = []

while(queue):
    a = queue.popleft()
    result.append(a+1)
    for i in graph[a]:
        indgree[i] -= 1
        if not indgree[i]:
            queue.append(i)

print(*result)