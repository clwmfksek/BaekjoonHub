import sys
input = sys.stdin.readline
import heapq

N,M,X = map(int,input().split())

graph = [[] for i in range(N+1)]
for i in range(M):
    n1,n2,n3 = map(int,input().split())
    graph[n1].append((n3,n2))

def dijkstra(start,end):
    d = [sys.maxsize] * (N+1)
    d[start] = 0

    pq = []
    heapq.heappush(pq,(0,start))    
    
    while(pq):
        dist,node = heapq.heappop(pq)
        if d[node] < dist : continue
        for cdist,cnode in graph[node]:
            ndist = cdist + dist
            if ndist < d[cnode]:
                d[cnode] = ndist
                heapq.heappush(pq,(ndist,cnode))
    return d[end]

maxvalue = 0
for i in range(1,N+1):
    maxvalue = max(maxvalue,dijkstra(i,X) + dijkstra(X,i))
print(maxvalue)