n,m = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
temp = []

def dfs(start):
    if len(temp)==m:
        print(*temp)
        return
    
    for i in range(start,n):
        if lis[i] not in temp:
            temp.append(lis[i])
            dfs(i+1)
            temp.pop()
dfs(0)