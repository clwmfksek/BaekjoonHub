import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

def dfs(num):
    for i in graph[num]:
        if visited[i] == 0:
            visited[i] = visited[num] + 1
            dfs(i)

n = int(input())
n1,n2 = map(int,input().split())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)
    
dfs(n1)
if visited[n2] == 0 : print(-1)
else : print(visited[n2])