n,m = map(int,input().split())
temp = []

def dfs(start):
    if len(temp)== m:
        print(*temp)
        return
    for i in range(start,n+1):
        temp.append(i)
        dfs(i)
        temp.pop()
dfs(1)