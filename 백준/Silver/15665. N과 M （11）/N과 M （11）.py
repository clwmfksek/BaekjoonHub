n,m = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
temp = []

def dfs():
    if len(temp)==m:
        print(*temp)
        return
    remember = 0
    for i in range(n):
        if remember != lis[i] :
            remember = lis[i]
            temp.append(lis[i])
            dfs()
            temp.pop()
dfs()