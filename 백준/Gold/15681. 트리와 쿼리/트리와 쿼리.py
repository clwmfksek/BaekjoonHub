import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,m,k = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if visited[i] == 0:
            visited[node] += dfs(i)
    return visited[node]

visited = [0 for i in range(n+1)]
dfs(m)
for i in range(k):
    num = int(input())
    print(visited[num])