import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x):
    global count
    visited[x] = 1
    temp.append(x)
    node = lis[x]
    if visited[node] == 0:
        dfs(node)
    elif visited[node] == 1:
        if node in temp:
            count += len(temp[temp.index(node):])

for _ in range(int(input())):
    n = int(input())
    lis = [0] + list(map(int,input().split()))
    count = 0
    visited = [0] * (n+1)
    for i in range(1,n+1):
       if not visited[i]:
           temp = []
           dfs(i)
    print(n-count)