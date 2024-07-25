import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

graph = []
visited = []

for i in range(n):
    v = list(input().rstrip())
    h = [0 for i in range(m)]
    graph.append(v)
    visited.append(h)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    global count
    if visited[i][j] == 1:
        return
    visited[i][j] = 1
    queue = deque([[i,j]])
    while(queue):
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if visited[nx][ny] == 1 or graph[nx][ny] == 'X':
                continue
            if graph[nx][ny] == 'P':
                count += 1

            visited[nx][ny] = 1
            queue.append([nx,ny])

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            bfs(i,j)
            if count == 0:
                print("TT")
            else :
                print(count)
            break