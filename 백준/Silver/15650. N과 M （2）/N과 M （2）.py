n,m = map(int,input().split())
visited = [0] * (n+1)
temp = []

def dfs(start):
    if len(temp)==m:
        print(*temp)
        return
    
    for i in range(start,n+1):
        if visited[i]: continue
        visited[i] = 1
        temp.append(i)
        dfs(i+1)
        temp.pop()
        visited[i] = 0
dfs(1)