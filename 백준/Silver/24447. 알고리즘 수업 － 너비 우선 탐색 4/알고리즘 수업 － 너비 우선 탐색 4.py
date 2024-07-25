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

def bfs(v,e,r):
    count = 1
    result = 0
    temp = [0] * (n+1)
    queue = deque([r])
    temp[r] = count
    v[r] = 0
    while(queue):
        u = queue.popleft()
        for i in sorted(e[u]):
            if(v[i] == -1):
                v[i] = v[u] + 1
                temp[i] = count +1
                count += 1
                queue.append(i)
    num = 0
    for i in range(1,n+1):
        result += v[i] * temp[i]
    print(result)

bfs(visited,graph,r)