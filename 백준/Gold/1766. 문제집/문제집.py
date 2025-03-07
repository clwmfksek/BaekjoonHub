from collections import deque
import heapq
n,m = map(int,input().split())

indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
queue = []

for i in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    indegree[n2] += 1

for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(queue,i)

while(queue):
    target = heapq.heappop(queue)
    print(target,end=' ')
    for i in graph[target]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue,i)