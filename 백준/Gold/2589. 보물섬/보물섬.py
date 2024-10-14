import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [list(input().rstrip()) for i in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    visited = [[0 for i in range(m)] for i in range(n)]
    visited[i][j] = 1
    maxsize = 0
    queue = deque([[i,j]])
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 'W' or visited[nx][ny] != 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append([nx,ny])
            maxsize = max(maxsize,visited[nx][ny])
    return maxsize
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            maxsize = bfs(i,j)
            cnt = max(cnt,maxsize)
print(cnt-1)