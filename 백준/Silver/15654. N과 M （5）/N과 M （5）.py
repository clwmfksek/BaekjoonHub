n,m = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
temp = []

def dfs():
    if len(temp)==m:
        print(*temp)
        return
    
    for i in range(n):
        if lis[i] not in temp:
            temp.append(lis[i])
            dfs()
            temp.pop()
dfs()