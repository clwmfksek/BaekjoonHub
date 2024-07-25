import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

graph = []
visited = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    visited.append([0 for i in range(m)])
rx = [-1,0,1,0,-1,1,1,-1]
ry = [0,1,0,-1,1,1,-1,-1]

def bfs(i,j):
    if visited[i][j] == 1: return
    queue = deque([[i,j]])
    global count
    count += 1
    while(queue):
        num1,num2 = queue.popleft()
        for i in range(8):
            x = num1 + rx[i]
            y = num2 + ry[i]
            if x >= n or y >= m or x < 0 or y < 0: continue
            if visited[x][y] == 1 or graph[x][y] == 0: continue
            visited[x][y] = 1
            queue.append([x,y])
count = 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            bfs(i,j)
print(count)