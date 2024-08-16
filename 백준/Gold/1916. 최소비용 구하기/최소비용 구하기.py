import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
start,end = map(int,input().split())

d = [sys.maxsize] * (n+1)
d[start] = 0

pq = []
heapq.heappush(pq,(start,0))

while pq:
    node, dist = heapq.heappop(pq)
    if d[node] < dist : continue
    for i,j in graph[node]:
        new_dist = dist + j
        if new_dist < d[i]:
            d[i] = new_dist
            heapq.heappush(pq,(i,new_dist))
print(d[end])        