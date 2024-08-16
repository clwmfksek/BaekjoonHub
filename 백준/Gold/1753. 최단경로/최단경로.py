import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
start = int(input())

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

d = [sys.maxsize] * (n+1)
d[start] = 0

# dijkstra
pq = []
heapq.heappush(pq,(0,start))

while pq:
    dist,node = heapq.heappop(pq)
    if d[node] < dist : continue
    for i,j in graph[node]:
        new_dist = dist + i
        if new_dist < d[j]:
            d[j] = new_dist
            heapq.heappush(pq,(new_dist,j))

for end in range(1,n+1):
    if d[end] == sys.maxsize : print("INF")
    else : print(d[end])        