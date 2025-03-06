n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(s1,s2):
    a = find(s1)
    b = find(s2)
    if a < b:
        parent[a] = b
    else :
        parent[b] = a

for _ in range(m):
    x,a,b = map(int,input().split())
    if not x :
        union(a,b)
    else :
        if find(a) == find(b):
            print("YES")
        else :
            print("NO")