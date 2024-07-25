import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())
visited = [-1] * (n+1)
versus = [0] * (n+1)
graph = [[] for _ in range(m+2)]
for i in range(m):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

def bfs(v,e,r):
    queue = deque([r])
    v[r] = 0
    while(queue):
        temp = queue.popleft()
        for i in e[temp]:
            if(v[i] == -1):
                v[i] = v[temp] + 1
                queue.append(i)
bfs(visited,graph,r)
for i in range(1,len(visited)):
    print(visited[i])