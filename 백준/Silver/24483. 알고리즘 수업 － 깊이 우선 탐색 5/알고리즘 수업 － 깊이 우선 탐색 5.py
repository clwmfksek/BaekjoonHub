import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())
visited = [-1] * (n+1)
visited2 = [-1] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

result = 0
count = 1  
visited2[r] = 0
def dfs(v,e,r):
    global count
    global result
    if not v[r]:
        v[r] = count
    for i in sorted(e[r]):
        if visited2[i] == -1:
            count += 1
            visited2[i] = (visited2[r] + 1)
            result += count * (visited2[r] + 1)
            dfs(v,e,i)

dfs(visited,graph,r)

print(result)