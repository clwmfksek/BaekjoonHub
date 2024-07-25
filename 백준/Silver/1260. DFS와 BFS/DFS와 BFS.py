import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,v = map(int,input().split())

visited = [0] * (n+1)
visited2 = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    num1,num2= map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

def dfs(v,e,r):
    v[r] = 1
    if r != 0:
        print(r, end=" ")
    for i in sorted(e[r]):
        if not v[i]:
            dfs(v,e,i)

def bfs(v,e,r):
    queue = deque([r])
    v[r] = 1
    while(queue):
        temp = queue.popleft()
        print(temp, end=" ")
        for i in sorted(e[temp]):
            if not v[i]:
                v[i] = 1
                queue.append(i)
dfs(visited,graph,v)
print()
bfs(visited2,graph,v)