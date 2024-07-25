n,m = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
visited = [0] * (n+1)
temp = []

def dfs():
    if len(temp)==m:
        print(*temp)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and lis[i] != remember:
            temp.append(lis[i])
            visited[i] = 1
            remember = lis[i]
            dfs()
            temp.pop()
            visited[i] = 0
dfs()