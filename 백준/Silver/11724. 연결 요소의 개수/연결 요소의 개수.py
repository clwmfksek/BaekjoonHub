import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

count = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)