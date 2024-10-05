import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

n,m = map(int,input().split())
graph = []
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x] : return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(a,b):
    x = find(a)
    y = find(b)
    if(x > y): 
        parent[x] = y
    else: 
        parent[y] = x

sumd = 0
for i in range(m):
    n1, n2, n3 = map(int, input().split())
    graph.append([n1, n2, n3])
    sumd += n3

graph.sort(key=lambda x: x[2])
mst_weight = 0
max_edge = 0

for i in range(m):
    s = graph[i][0]
    e = graph[i][1]
    w = graph[i][2]
    
    if find(s) != find(e):
        merge(s, e)
        mst_weight += w

dest = find(1)
bol = False
for i in range(2,n+1):
    st = find(i)
    if dest != st : 
        bol = True
        break
if bol : print(-1)
else : print(sumd - mst_weight)