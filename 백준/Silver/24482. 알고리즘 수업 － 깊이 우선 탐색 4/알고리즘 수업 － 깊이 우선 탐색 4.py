import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())
visited = [-1] * (n+1)
graph = [[] for _ in range(m+2)]
for i in range(m):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

visited[r] = 0
def dfs(v,e,r):
    for i in sorted(e[r])[::-1]:
        if(v[i] == -1):
            visited[i] = visited[r] + 1
            dfs(v,e,i)

dfs(visited,graph,r)
for i in range(1,len(visited)):
    print(visited[i])