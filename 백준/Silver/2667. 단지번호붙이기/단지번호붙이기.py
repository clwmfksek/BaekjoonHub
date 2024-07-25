import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
visited = []
result = []
for i in range(n):
    lis = list(input().rstrip())
    lis = list(map(int,lis))
    graph.append(lis)
    visited.append([0]*n)

rx = [-1,0,1,0]
ry = [0,1,0,-1]
world_count = 0

def bfs(i,j):
    global world_count
    if visited[i][j] == 1: return 0
    count = 1
    world_count += 1
    visited[i][j] = 1
    queue = deque([[i,j]])
    while(queue):
        num1,num2 = queue.popleft()
        for i in range(4):
            x = num1 + rx[i]
            y = num2 + ry[i]
            if x < 0 or y < 0 or x > n-1 or y > n-1 : continue
            if visited[x][y] == 1 or graph[x][y] == 0: continue
            count += 1
            visited[x][y] = 1
            queue.append([x,y])
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i,j))
print(world_count)
for i in sorted(result):
    if i != 0 :
        print(i)