import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m,n = map(int,input().split())
graph = []
visited = []

for i in range(m):
    v = list(map(int,input().split()))
    graph.append(v)
    p = [0 for i in range(n)]
    visited.append(p)

rx = [-1,0,1,0]
ry = [0,1,0,-1]

def bfs(i,j):
    if(visited[i][j] == 1 or graph[i][j] == 0): return
    visited[i][j] = 1
    queue = deque([[i,j]])
    global count
    global count1
    count += 1
    while(queue):
        num1,num2 = queue.popleft()
        for i in range(4):
            x = num1 + rx[i]
            y = num2 + ry[i]
            if(x<0 or y<0 or x>=m or y>=n): continue
            if(visited[x][y] == 1 or graph[x][y] == 0): continue
            visited[x][y] = 1
            count += 1
            queue.append([x,y])
    count1 += 1

maxx = 0
count1 = 0
for i in range(m):
    for j in range(n):
        count = 0
        bfs(i,j)
        if count > maxx: maxx =count     
print(count1)
print(maxx)