import sys
input = sys.stdin.readline
n,m = map(int,input().split())

lis = [[] for i in range(n)]
visited = [0] * n

for i in range(m):
    n1,n2 = map(int,input().split())
    lis[n1].append(n2)
    lis[n2].append(n1)

found = False
result = []
def dfs(num):
    global found
    if found:
        return
    if len(result) == 5:
        found = True
        return
    for i in lis[num]:
        if visited[i] == 0:
            result.append(i)
            visited[i] = 1
            dfs(i)
            result.pop()
            visited[i] = 0

for i in range(n):
    result.append(i)
    visited[i] = 1
    dfs(i)
    result.pop()
    visited[i] = 0
print(1 if found else 0)