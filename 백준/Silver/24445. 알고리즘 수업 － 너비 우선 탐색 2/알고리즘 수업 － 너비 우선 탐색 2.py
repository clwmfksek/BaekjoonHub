import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())
visited = [0] * (n+1)
graph = [[] for _ in range(m+2)]
for i in range(m):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

count = 1

def bfs(v,e,r):
    global count
    queue = deque([r])
    v[r] = count
    count += 1
    while(queue):
        temp = queue.popleft()
        for i in sorted(e[temp])[::-1]:
            if(v[i] == 0):
                v[i] = count
                count += 1
                queue.append(i)

bfs(visited,graph,r)

for i in range(1,len(visited)):
    print(visited[i])