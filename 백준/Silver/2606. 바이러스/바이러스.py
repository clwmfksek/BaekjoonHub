computer = int(input())
network = int(input())
count = 0

def dfs(g,v,visited):
    visited[v] = 1
    for i in g[v]:
        if not visited[i]:
            dfs(g,i,visited)

lis = [0] * (computer+1)
lis2 = [[] for _ in range(computer+1)]
for _ in range(network):
    num1,num2 = map(int,input().split())
    lis2[num1] += [num2]
    lis2[num2] += [num1]
dfs(lis2,1,lis)
print(sum(lis)-1)