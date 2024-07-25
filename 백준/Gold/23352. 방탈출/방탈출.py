import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n,m = map(int,input().split())
graph = []
visited = [[0]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,input().split())))

rx = [1,0,-1,0]
ry = [0,1,0,-1]


def bfs(s,f):
    global longvisit
    global plusvalue
    global startvalue
    visited = [[0]*m for _ in range(n)]
    visited[s][f] = 1
    queue = deque([(s,f)])
    startvalue = graph[s][f]
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            nx = x + rx[i]
            ny = y + ry[i]
            if nx>=n or ny>=m or nx<0 or ny<0: continue
            if visited[nx][ny] > 0 or graph[nx][ny] == 0 : continue
            visited[nx][ny] = visited[x][y] + 1
            if visited[nx][ny] > longvisit:
                longvisit = visited[nx][ny]
                plusvalue = graph[nx][ny]
            queue.append((nx,ny))
    result.append([longvisit,graph[s][f]+plusvalue])
cou = 0
cout = 0
count = 0
plusvalue = 0
longvisit = 0
startvalue = 0
result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            longvisit= 0 
            bfs(i,j)
result.sort(key=lambda x : (x[0],x[1]),reverse=True)
print(result[0][1])