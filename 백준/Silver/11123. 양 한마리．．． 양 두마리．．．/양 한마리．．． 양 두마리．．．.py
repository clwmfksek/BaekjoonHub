import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

rx = [-1,0,1,0]
ry = [0,1,0,-1]

def bfs(i,j):
    if visited[i][j] == 1 : return
    global count
    count += 1
    visited[i][j] = 1
    queue = deque([[i,j]])
    while(queue):
        n1,n2 = queue.popleft()
        for index in range(4):
            x = n1 + rx[index]
            y = n2 + ry[index]
            if(x>=num1 or y>=num2 or x<0 or y<0): continue
            if(visited[x][y] == 1 or graph[x][y] == "."): continue
            visited[x][y] = 1
            queue.append([x,y])

t = int(input())
for _ in range(t):
    graph = []
    visited = []

    num1,num2 = map(int,input().split())
    for i in range(num1):
        graph.append(list(input().rstrip()))
        visited.append([0 for i in range(num2)])
    count = 0
    for i in range(num1):
        for j in range(num2):
            if(graph[i][j] == "#"): bfs(i,j)
    print(count)
