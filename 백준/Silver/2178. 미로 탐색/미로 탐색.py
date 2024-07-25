import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

graph = []
visited = []

for i in range(n):
    v = list(input().rstrip())
    v = list(map(int,v))
    graph.append(v)

for i in range(n):
    v = [0 for i in range(m)]
    visited.append(v)

def bfs(s,t):
    visited[s][t] = 1
    queue = deque([[s,t]])
    count = 0
    rx = [-1,0,1,0]
    ry = [0,1,0,-1]

    while(queue):
        temp = queue.popleft()
        for i in range(4):
            x = temp[0] + rx[i]
            y = temp[1] + ry[i]
            if x < 0 or y < 0 or x > n-1 or y > m-1:
                continue
            if visited[x][y] != 0 or graph[x][y] == 0:
                continue
            visited[x][y] += visited[temp[0]][temp[1]] + 1
            queue.append([x,y])
    print(visited[n-1][m-1])
bfs(0,0)