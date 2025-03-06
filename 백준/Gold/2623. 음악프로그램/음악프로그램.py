import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)
queue = deque()
result = []

for i in range(m):
    temp = list(map(int,input().split()))
    for j in range(1,temp[0]):
        graph[temp[j]].append(temp[j+1])
        indegree[temp[j+1]] += 1

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

while(queue):
    target = queue.popleft()
    result.append(target)
    for i in graph[target]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
if len(result) != n : print(0)
else :
    for i in result:
        print(i)