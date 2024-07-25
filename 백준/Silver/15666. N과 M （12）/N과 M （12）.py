n,m = map(int,input().split())
lis = list(set(list(map(int,input().split()))))
lis.sort()
temp = []

def dfs(start):
    if len(temp)==m:
        print(*temp)
        return
    
    for i in range(start,len(lis)):
        temp.append(lis[i])
        dfs(i)
        temp.pop()
dfs(0)