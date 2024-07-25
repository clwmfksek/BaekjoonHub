import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,k = map(int,input().split())

graph = []
visited = []
for i in range(n):
    graph.append([0 for i in range(m)])
    visited.append([0 for i in range(m)])

for i in range(k):
    num1,num2 = map(int,input().split())
    graph[num1-1][num2-1] = 1

rx = [-1,0,1,0]
ry = [0,1,0,-1]

def bfs(i,j):
    if visited[i][j] == 1: return
    visited[i][j] = 1
    queue = deque([[i,j]])
    global count
    while(queue):
        n1,n2 = queue.popleft()
        for i in range(4):
            x = n1 + rx[i]
            y = n2 + ry[i]
            if x >= n or y >= m or x < 0 or y < 0: continue
            if visited[x][y] == 1 or graph[x][y] == 0: continue
            count += 1
            visited[x][y] = 1
            queue.append([x,y])
maxx = 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            count = 1
            bfs(i,j)
            if count > maxx: maxx = count
print(maxx)