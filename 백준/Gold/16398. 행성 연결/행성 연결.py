import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

n = int(input())
graph = [list(map(int,input().split())) for i in range(n)]
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x] : return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    x = find(a)
    y = find(b)
    if(x>y) : parent[x] = y
    else : parent[y] = x

target = []

for i in range(n):
    for j in range(n):
        target.append([i,j,graph[i][j]])

target.sort(key=lambda x: x[2])
ans = 0
cnt = 0

for i in range(len(target)):
    s = target[i][0]
    e = target[i][1]
    if(find(s) != find(e)):
        merge(s,e)
        ans += target[i][2]
        cnt += 1
    if cnt == n-1 : break
print(ans)