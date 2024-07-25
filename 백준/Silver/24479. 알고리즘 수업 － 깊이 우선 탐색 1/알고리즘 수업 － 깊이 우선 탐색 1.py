import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

count = 1  

def dfs(v,e,r):
    global count
    if not v[r]:
        v[r] = count
        count += 1
    for i in sorted(e[r]):
        if not v[i]:
            dfs(v,e,i)

dfs(visited,graph,r)

for i in range(1,len(visited)):
    print(visited[i])