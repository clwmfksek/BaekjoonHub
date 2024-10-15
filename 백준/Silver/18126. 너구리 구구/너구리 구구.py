import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visited = [0 for i in range(n+1)]
queue = deque([1])
while(queue):
    s = queue.popleft()
    for i in graph[s]:
        if visited[i[0]] == 0:
            visited[i[0]] = max(visited[i[0]],visited[s] + i[1])
            queue.append(i[0])
print(max(visited))