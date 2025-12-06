import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                visited[n] = visited[node] + 1
                queue.append(n)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [0] * (N+1)
bfs(1)
m = max(visited)
print(visited.index(m), m-1, visited.count(m))