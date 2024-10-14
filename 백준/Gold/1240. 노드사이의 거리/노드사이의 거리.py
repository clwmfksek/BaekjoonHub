import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(m):
    n1,n2 = map(int,input().split())
    visited = [0 for i in range(n+1)]
    visited[n1] = 0
    q = deque([(n1)])
    while q:
        node = q.popleft()
        if node == n2:
            print(visited[node])
            break
        for j in graph[node]:
            if visited[j[0]] == 0 :
                visited[j[0]] = visited[node] + j[1]
                q.append(j[0])
